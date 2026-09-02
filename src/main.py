"""Google Trending Now — Apify Actor.

Fetches real-time Google Trends data via the Scrape.do Google Trends API
and pushes the results into an Apify Dataset.
"""

import asyncio
import os
from typing import Any, Dict

import httpx
from apify import Actor

# Scrape.do Google Trends endpoint
API_URL = "https://api.scrape.do/plugin/google/trending"

# Request configuration
REQUEST_TIMEOUT = 30


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

        geo: str = input_data.get("geo", "US") or "US"
        hl: str = input_data.get("hl", "en") or "en"
        hours: int = int(input_data.get("hours", "24") or "24")
        cat: int = int(input_data.get("cat", "0") or "0")
        sort: str = input_data.get("sort", "relevance") or "relevance"
        status: str = input_data.get("status", "all") or "all"

        Actor.log.info(
            f"Configuration — geo={geo}, hl={hl}, hours={hours}, "
            f"cat={cat}, sort={sort}, status={status}"
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
        Actor.log.info(f"Requesting {API_URL} ...")

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

        # ── 5. Push to Dataset ──────────────────────────────────────
        Actor.log.info("Pushing each trend as an individual record to Dataset")
        for trend in trends:
            trend["search_parameters"] = search_parameters
        await Actor.push_data(trends)
        Actor.log.info(f"Pushed {len(trends)} trend records to Dataset")

        # ── 6. Done ─────────────────────────────────────────────────
        Actor.log.info("=" * 60)
        Actor.log.info("ACTOR COMPLETED SUCCESSFULLY")
        Actor.log.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
