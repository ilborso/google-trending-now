"""Google Trending Now — Apify Actor.

Fetches real-time Google Trends data via the Scrape.do Google Trends API
and pushes the results into an Apify Dataset.
"""

import asyncio
import json
import os
from typing import Any, Dict, List

import httpx
from apify import Actor
from google import genai
from google.genai import types

# Scrape.do Google Trends endpoint
API_URL = "https://api.scrape.do/plugin/google/trending"

# Request configuration
REQUEST_TIMEOUT = 30

# Category ID to description mapping
CATEGORY_MAP: Dict[int, str] = {
    0: "All categories",
    1: "Autos and Vehicles",
    2: "Beauty and Fashion",
    3: "Business and Finance",
    4: "Entertainment",
    5: "Food and Drink",
    6: "Games",
    7: "Health",
    8: "Hobbies and Leisure",
    9: "Jobs and Education",
    10: "Law and Government",
    11: "Other",
    13: "Pets and Animals",
    14: "Politics",
    15: "Science",
    16: "Shopping",
    17: "Sports",
    18: "Technology",
    19: "Travel and Transportation",
    20: "Climate",
}

DEFAULT_SYSTEM_INSTRUCTION = """
Sei un Senior Marketing Intelligence Analyst. Il tuo compito è analizzare una lista di ricerche di tendenza estratte da Google Trends e generare insight operativi rapidi per i team di marketing, content creation e paid media.

Devi analizzare ciascun trend e restituire ESCLUSIVAMENTE un array JSON di oggetti. Non aggiungere testo introduttivo, spiegazioni o blocchi discorsivi.

Per ogni elemento analizzato, genera l'oggetto con questa struttura:
- "title": (stringa, esattamente uguale al title di input)
- "ai_marketing_intelligence": {
    "why_it_matters": (stringa sintetica: max 15 parole sul contesto o evento scatenante più probabile),
    "affected_sectors": (array di 2-3 stringhe con i settori merceologici o verticali rilevanti, es: "E-commerce", "Food", "Sport Media"),
    "marketing_angle": (stringa: 1 idea tattica di newsjacking, piano editoriale o content creation),
    "paid_ads_advice": (stringa: raccomandazione per Google Ads/Meta Ads, es. "Aggiungere come parola chiave negativa", "Aumentare bid su query correlate", o "Nessuna azione"),
    "brand_safety_risk": (stringa tra: "Low", "Medium", "High")
  }

Mantieni i testi concisi, asciutti e orientati all'azione. Rispondi solo in lingua italiana.
"""


def enrich_trends_with_ai(
    trends_data: List[Dict[str, Any]],
    api_key: str,
    system_instruction: str,
    model: str,
    temperature: float,
) -> List[Dict[str, Any]]:
    if not trends_data:
        return []

    client = genai.Client(api_key=api_key)

    # Per minimizzare i token inviati all'LLM, estraiamo solo le chiavi essenziali
    lean_input = [
        {
            "title": item.get("title"),
            "category_description": item.get("category_description"),
            "growth_percentage": item.get("growth_percentage"),
        }
        for item in trends_data
    ]

    user_prompt = f"Analizza il seguente array di trend e restituisci l'array JSON arricchito:\n{json.dumps(lean_input, ensure_ascii=False)}"

    response = client.models.generate_content(
        model=model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            temperature=temperature,
        ),
    )

    # Parsing dell'output generato
    raw_text = response.text.strip() if response.text else "[]"
    try:
        ai_output = json.loads(raw_text)
    except Exception as exc:
        Actor.log.warning(f"Failed to parse JSON output from Gemini: {exc}")
        ai_output = []

    # Mappa per lookup O(1) sul campo title
    ai_map = {}
    if isinstance(ai_output, list):
        for item in ai_output:
            if isinstance(item, dict) and "title" in item and item["title"]:
                ai_map[str(item["title"]).strip().lower()] = item.get("ai_marketing_intelligence")

    # Merge dei dati nel dataset originale dell'Actor
    enriched_dataset = []
    for trend in trends_data:
        lookup_key = str(trend.get("title", "")).strip().lower()
        trend_copy = dict(trend)
        trend_copy["ai_marketing_intelligence"] = ai_map.get(lookup_key)
        enriched_dataset.append(trend_copy)

    return enriched_dataset


async def main() -> None:
    """Main entry point of the Actor."""
    async with Actor:
        Actor.log.info("=" * 60)
        Actor.log.info("GOOGLE TRENDING NOW ACTOR STARTED")
        Actor.log.info("=" * 60)

        # ── 1. Read and validate input ──────────────────────────────
        input_data: Dict[str, Any] = await Actor.get_input() or {}

        token = os.environ.get("SCRAPEDO_TOKEN", "").strip()
        if not token:
            await Actor.fail(
                status_message="Missing SCRAPEDO_TOKEN environment variable. "
                "Please set it in the Actor's Environment Variables settings."
            )
            return  # unreachable, but keeps the type checker happy

        ai_marketing_intelligence: bool = bool(input_data.get("AI_Marketing_Intelligence", False))
        gemini_api_key = os.environ.get("GEMINI_API_KEY", "").strip()
        if ai_marketing_intelligence and not gemini_api_key:
            await Actor.fail(
                status_message="Missing GEMINI_API_KEY environment variable. "
                "AI_Marketing_Intelligence is enabled, but GEMINI_API_KEY is not set."
            )
            return

        geo: str = input_data.get("geo", "US") or "US"
        hl: str = input_data.get("hl", "en") or "en"
        hours: int = int(input_data.get("hours", "24") or "24")
        cat: int = int(input_data.get("cat", "0") or "0")
        sort: str = input_data.get("sort", "relevance") or "relevance"
        status: str = input_data.get("status", "all") or "all"

        raw_max_items = input_data.get("max_items")
        max_items: int = 2000
        if raw_max_items is not None:
            try:
                max_items = int(raw_max_items)
            except (ValueError, TypeError):
                max_items = 2000
        if max_items <= 0:
            max_items = 2000

        Actor.log.info(
            f"Configuration — geo={geo}, hl={hl}, hours={hours}, "
            f"cat={cat}, sort={sort}, status={status}, max_items={max_items}, "
            f"AI_Marketing_Intelligence={ai_marketing_intelligence}"
        )

        # ── 2. Build query parameters ──────────────────────────────
        params: Dict[str, Any] = {
            "token": token,
            "geo": geo,
            "hl": hl,
            "hours": hours,
            "cat": cat,
            "sort": sort,
            "status": status,
        }

        # ── 3. Make the API request ─────────────────────────────────
        Actor.log.info("Elaborating on Google Trending ...")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    API_URL,
                    params=params,
                    timeout=REQUEST_TIMEOUT,
                )
        except httpx.TimeoutException:
            await Actor.fail(
                status_message=f"Request timed out after {REQUEST_TIMEOUT}s. "
                "The Scrape.do API did not respond in time."
            )
            return
        except httpx.NetworkError as exc:
            await Actor.fail(
                status_message=f"Network error while contacting Scrape.do API: {exc}"
            )
            return

        Actor.log.info(f"Response status: {response.status_code}")

        if response.status_code >= 400:
            body_preview = response.text[:500] if response.text else "(empty body)"
            await Actor.fail(
                status_message=f"Scrape.do API returned HTTP {response.status_code}. "
                f"Response: {body_preview}"
            )
            return

        # ── 4. Parse response ───────────────────────────────────────
        try:
            data: Dict[str, Any] = response.json()
        except Exception as exc:
            await Actor.fail(
                status_message=f"Failed to parse JSON from Scrape.do API response: {exc}"
            )
            return

        trends = data.get("trends", [])
        search_parameters = data.get("search_parameters", {})

        Actor.log.info(f"Received {len(trends)} trends from the API")

        if len(trends) > max_items:
            Actor.log.info(f"Limiting trends to max_items={max_items} (from {len(trends)})")
            trends = trends[:max_items]

        # ── 5. Prepare trends records ───────────────────────────────
        for trend in trends:
            trend["search_parameters"] = search_parameters
            # Resolve category IDs to human-readable descriptions
            cat_ids = trend.get("category_ids", [])
            trend["category_description"] = [
                CATEGORY_MAP.get(cid, f"Unknown ({cid})") for cid in cat_ids
            ]

        # ── 6. AI Marketing Intelligence Enrichment ─────────────────
        if ai_marketing_intelligence:
            Actor.log.info("Enriching trends with AI Marketing Intelligence using Gemini API...")
            system_instruction = os.environ.get("AI_MARKETING_PROMPT", "").strip() or DEFAULT_SYSTEM_INSTRUCTION
            model = os.environ.get("MODEL", "").strip() or "gemini-2.5-flash-lite"
            raw_temp = os.environ.get("AI_MARKETING_TEMPERATURE", "0.2")
            try:
                temperature = float(raw_temp)
            except (ValueError, TypeError):
                temperature = 0.2

            try:
                trends = enrich_trends_with_ai(
                    trends_data=trends,
                    api_key=gemini_api_key,
                    system_instruction=system_instruction,
                    model=model,
                    temperature=temperature,
                )
            except Exception as exc:
                await Actor.fail(
                    status_message=f"AI Marketing Intelligence processing failed: {exc}"
                )
                return

        # ── 7. Push to Dataset ──────────────────────────────────────
        Actor.log.info("Pushing each trend as an individual record to Dataset")
        await Actor.push_data(trends)
        Actor.log.info(f"Pushed {len(trends)} trend records to Dataset")

        # ── 8. Done ─────────────────────────────────────────────────
        Actor.log.info("=" * 60)
        Actor.log.info("ACTOR COMPLETED SUCCESSFULLY")
        Actor.log.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
