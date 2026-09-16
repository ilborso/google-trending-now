# Google Trending Now

An Apify Actor that fetches real-time Google Trends data and saves the results to an Apify Dataset. Optionaly you can Enable AI-generated marketing intelligence insights via Google Gemini.

## What does this Actor do?

This Actor:
1. Accepts configurable parameters (country, language, time window, category, sort order, status)
2. Fetches the latest trending searches from Google Trends
3. Returns structured data including titles, search volumes, growth percentages, and related queries. 
4. Perform for each terms a marketing analisys with a short description of the trend context or trigger (max 15 words) relevant industry verticals (2-3 items), tactical idea for newsjacking, editorial plan, or content creation, recommendation for Google Ads / Meta Ads, risk level for brand safety.

Perfect for trend monitoring, content strategy, SEO research, market analysis, and real-time search intelligence.

## Why use Google Trending Now?

- **Real-time data** — Access the latest Google Trends data as it happens
- **Flexible filtering** — Filter by country, language, time window, category, and status
- **Multiple sort options** — Sort by relevance, search volume, recency, or title
- **Embedded AI Marketing intelligence** - AI Marketing analisys for each record via latest Gemini Flash Lite.
- **Two output modes** — Get the full response or flattened records for easy table viewing
- **20 category filters** — From Sports and Technology to Politics and Climate
- **Production-ready** — Clean error handling with descriptive failure messages

## Input Schema

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `geo` | string | Yes | `"US"` | Two-letter country code (see table below) |
| `hl` | string | No | `"en"` | Language code (e.g. `en`, `it`, `es`, `de`, ... see table below) |
| `hours` | integer | No | `24` | Time window. Options: `4`, `24`, `48`, `168` |
| `cat` | integer | No | `0` | Category ID filter (see table below) |
| `sort` | string | No | `"relevance"` | Sort order: `relevance`, `search_volume`, `recency`, `title` |
| `status` | string | No | `"all"` | Trend status filter: `all`, `active` |
| `max_items` | integer | No | `2000` | Maximum number of trending items to return |
| `AI_Marketing_Intelligence` | boolean | No | `false` | Enable AI-generated marketing intelligence insights via Google Gemini. This impacts the scraper's performance, as it includes the LLM's processing time.  |

See some example: 

| Description | `cat` | `geo` | `hl` | `hours` | `sort` | `status` | JSON Input |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| All trending topics in the US, last 24 hours | `0` | `US` | `en` | `24` | `relevance` | `all` | `{"cat": "0", "geo": "US", "hl": "en", "hours": "24", "sort": "relevance", "status": "all"}` |
| Sports trends in the UK, last 48 hours, order by search volume | `17` | `GB` | `en` | `48` | `search_volume` | `all` | `{"cat": "17", "geo": "GB", "hl": "en", "hours": "48", "sort": "search_volume", "status": "all"}` |
| Active entertainment trends sorted by search volume, status active | `4` | `US` | `en` | `48` | `relevance` | `active` | `{"cat": "4", "geo": "US", "hl": "en", "hours": "48", "sort": "relevance", "status": "active"}` |
| Trending in Germany, last 7 days, in German, order by search volume, status active | `0` | `DE` | `en` | `168` | `search_volume` | `active` | `{"cat": "0", "geo": "DE", "hl": "en", "hours": "168", "sort": "search_volume", "status": "active"}` |
| Technology trends, most recent first | `0` | `DE` | `en` | `168` | `recency` | `active` | `{"cat": "0", "geo": "DE", "hl": "en", "hours": "168", "sort": "recency", "status": "active"}` |

### Category IDs

| ID | Category |
|----|----------|
| 0 | All categories |
| 1 | Autos and Vehicles |
| 2 | Beauty and Fashion |
| 3 | Business and Finance |
| 4 | Entertainment |
| 5 | Food and Drink |
| 6 | Games |
| 7 | Health |
| 8 | Hobbies and Leisure |
| 9 | Jobs and Education |
| 10 | Law and Government |
| 11 | Other |
| 13 | Pets and Animals |
| 14 | Politics |
| 15 | Science |
| 16 | Shopping |
| 17 | Sports |
| 18 | Technology |
| 19 | Travel and Transportation |
| 20 | Climate |

### Country Code

| Country Code | Description | Country Code | Description | Country Code | Description | Country Code | Description | Country Code | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AD | Andorra | AE | United Arab Emirates | AF | Afghanistan | AG | Antigua and Barbuda | AI | Anguilla |
| AL | Albania | AM | Armenia | AO | Angola | AQ | Antarctica | AR | Argentina |
| AS | American Samoa | AT | Austria | AU | Australia | AW | Aruba | AX | Åland Islands |
| AZ | Azerbaijan | BA | Bosnia and Herzegovina | BB | Barbados | BD | Bangladesh | BE | Belgium |
| BF | Burkina Faso | BG | Bulgaria | BH | Bahrain | BI | Burundi | BJ | Benin |
| BL | Saint Barthélemy | BM | Bermuda | BN | Brunei Darussalam | BO | Bolivia | BQ | Bonaire, Sint Eustatius and Saba |
| BR | Brazil | BS | Bahamas | BT | Bhutan | BV | Bouvet Island | BW | Botswana |
| BY | Belarus | BZ | Belize | CA | Canada | CC | Cocos (Keeling) Islands | CD | Democratic Republic of the Congo |
| CF | Central African Republic | CG | Republic of the Congo | CH | Switzerland | CI | Côte d'Ivoire | CK | Cook Islands |
| CL | Chile | CM | Cameroon | CN | China | CO | Colombia | CR | Costa Rica |
| CU | Cuba | CV | Cabo Verde | CW | Curaçao | CX | Christmas Island | CY | Cyprus |
| CZ | Czechia | DE | Germany | DJ | Djibouti | DK | Denmark | DM | Dominica |
| DO | Dominican Republic | DZ | Algeria | EC | Ecuador | EE | Estonia | EG | Egypt |
| EH | Western Sahara | ER | Eritrea | ES | Spain | ET | Ethiopia | FI | Finland |
| FJ | Fiji | FK | Falkland Islands | FM | Micronesia | FO | Faroe Islands | FR | France |
| GA | Gabon | GB | United Kingdom | GD | Grenada | GE | Georgia | GF | French Guiana |
| GG | Guernsey | GH | Ghana | GI | Gibraltar | GL | Greenland | GM | Gambia |
| GN | Guinea | GP | Guadeloupe | GQ | Equatorial Guinea | GR | Greece | GS | South Georgia and the South Sandwich Islands |
| GT | Guatemala | GU | Guam | GW | Guinea-Bissau | GY | Guyana | HK | Hong Kong |
| HM | Heard Island and McDonald Islands | HN | Honduras | HR | Croatia | HT | Haiti | HU | Hungary |
| ID | Indonesia | IE | Ireland | IL | Israel | IM | Isle of Man | IN | India |
| IO | British Indian Ocean Territory | IQ | Iraq | IR | Iran | IS | Iceland | IT | Italy |
| JE | Jersey | JM | Jamaica | JO | Jordan | JP | Japan | KE | Kenya |
| KG | Kyrgyzstan | KH | Cambodia | KI | Kiribati | KM | Comoros | KN | Saint Kitts and Nevis |
| KP | North Korea | KR | South Korea | KW | Kuwait | KY | Cayman Islands | KZ | Kazakhstan |
| LA | Laos | LB | Lebanon | LC | Saint Lucia | LI | Liechtenstein | LK | Sri Lanka |
| LR | Liberia | LS | Lesotho | LT | Lithuania | LU | Luxembourg | LV | Latvia |
| LY | Libya | MA | Morocco | MC | Monaco | MD | Moldova | ME | Montenegro |
| MF | Saint Martin | MG | Madagascar | MH | Marshall Islands | MK | North Macedonia | ML | Mali |
| MM | Myanmar | MN | Mongolia | MO | Macao | MP | Northern Mariana Islands | MQ | Martinique |
| MR | Mauritania | MS | Montserrat | MT | Malta | MU | Mauritius | MV | Maldives |
| MW | Malawi | MX | Mexico | MY | Malaysia | MZ | Mozambique | NA | Namibia |
| NC | New Caledonia | NE | Niger | NF | Norfolk Island | NG | Nigeria | NI | Nicaragua |
| NL | Netherlands | NO | Norway | NP | Nepal | NR | Nauru | NU | Niue |
| NZ | New Zealand | OM | Oman | PA | Panama | PE | Peru | PF | French Polynesia |
| PG | Papua New Guinea | PH | Philippines | PK | Pakistan | PL | Poland | PM | Saint Pierre and Miquelon |
| PN | Pitcairn | PR | Puerto Rico | PS | Palestine | PT | Portugal | PW | Palau |
| PY | Paraguay | QA | Qatar | RE | Réunion | RO | Romania | RS | Serbia |
| RU | Russia | RW | Rwanda | SA | Saudi Arabia | SB | Solomon Islands | SC | Seychelles |
| SD | Sudan | SE | Sweden | SG | Singapore | SH | Saint Helena, Ascension and Tristan da Cunha | SI | Slovenia |
| SJ | Svalbard and Jan Mayen | SK | Slovakia | SL | Sierra Leone | SM | San Marino | SN | Senegal |
| SO | Somalia | SR | Suriname | SS | South Sudan | ST | Sao Tome and Principe | SV | El Salvador |
| SX | Sint Maarten | SY | Syria | SZ | Eswatini | TC | Turks and Caicos Islands | TD | Chad |
| TF | French Southern Territories | TG | Togo | TH | Thailand | TJ | Tajikistan | TK | Tokelau |
| TL | Timor-Leste | TM | Turkmenistan | TN | Tunisia | TO | Tonga | TR | Türkiye |
| TT | Trinidad and Tobago | TV | Tuvalu | TW | Taiwan | TZ | Tanzania | UA | Ukraine |
| UG | Uganda | UM | United States Minor Outlying Islands | US | United States | UY | Uruguay | UZ | Uzbekistan |
| VA | Holy See | VC | Saint Vincent and the Grenadines | VE | Venezuela | VG | Virgin Islands (British) | VI | Virgin Islands (U.S.) |
| VN | Viet Nam | VU | Vanuatu | WF | Wallis and Futuna | WS | Samoa | YE | Yemen |
| YT | Mayotte | ZA | South Africa | ZM | Zambia | ZW | Zimbabwe | | |


### Language Code

| Language Code | Description | Language Code | Description | Language Code | Description | Language Code | Description | Language Code | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| aa | Afar | ab | Abkhazian | af | Afrikaans | am | Amharic | ar | Arabic |
| as | Assamese | ay | Aymara | az | Azerbaijani | ba | Bashkir | be | Belarusian |
| bg | Bulgarian | bh | Bihari | bi | Bislama | bn | Bengali | bo | Tibetan |
| br | Breton | ca | Catalan | co | Corsican | cs | Czech | cy | Welsh |
| da | Danish | de | German | dz | Bhutani | el | Greek | en | English |
| eo | Esperanto | es | Spanish | et | Estonian | eu | Basque | fa | Persian |
| fi | Finnish | fj | Fiji | fo | Faroese | fr | French | fy | Frisian |
| ga | Irish | gd | Scots Gaelic | gl | Galician | gn | Guarani | gu | Gujarati |
| ha | Hausa | he | Hebrew | hi | Hindi | hr | Croatian | hu | Hungarian |
| hy | Armenian | ia | Interlingua | id | Indonesian | ie | Interlingue | ik | Inupiak |
| is | Icelandic | it | Italian | iu | Inuktitut | ja | Japanese | jw | Javanese |
| ka | Georgian | kk | Kazakh | kl | Greenlandic | km | Cambodian | kn | Kannada |
| ko | Korean | ks | Kashmiri | ku | Kurdish | ky | Kirghiz | la | Latin |
| ln | Lingala | lo | Laothian | lt | Lithuanian | lv | Latvian | mg | Malagasy |
| mi | Maori | mk | Macedonian | ml | Malayalam | mn | Mongolian | mo | Moldavian |
| mr | Marathi | ms | Malay | mt | Maltese | my | Burmese | na | Nauru |
| ne | Nepali | nl | Dutch | no | Norwegian | oc | Occitan | om | Oromo |
| or | Oriya | pa | Punjabi | pl | Polish | ps | Pashto | pt | Portuguese |
| qu | Quechua | rm | Rhaeto-Romance | rn | Kirundi | ro | Romanian | ru | Russian |
| rw | Kinyarwanda | sa | Sanskrit | sd | Sindhi | sg | Sangro | sh | Serbo-Croatian |
| si | Singhalese | sk | Slovak | sl | Slovenian | sm | Samoan | sn | Shona |
| so | Somali | sq | Albanian | sr | Serbian | ss | Siswati | st | Sesotho |
| su | Sundanese | sv | Swedish | sw | Swahili | ta | Tamil | te | Telugu |
| tg | Tajik | th | Thai | ti | Tigrinya | tk | Turkmen | tl | Tagalog |
| tn | Setswana | to | Tonga | tr | Turkish | ts | Tsonga | tt | Tatar |
| tw | Twi | ug | Uighur | uk | Ukrainian | ur | Urdu | uz | Uzbek |
| vi | Vietnamese | vo | Volapuk | wo | Wolof | xh | Xhosa | yi | Yiddish |
| yo | Yoruba | za | Zhuang | zh | Chinese | zu | Zulu | | |

## Output Schema

| Field | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | The trending search topic |
| `search_volume` | `integer` | Approximate search volume |
| `growth_percentage` | `integer` | Percentage growth in search interest |
| `started_at` | `integer` | Unix timestamp when the trend started |
| `ended_at` | `integer` | Unix timestamp when the trend ended. Omitted if still active |
| `status` | `string` | active or ended |
| `related_queries` | `string[]` | Related search queries. May be empty |
| `category_ids` | `integer[]` | Category IDs this trend belongs to. May be empty |
| `trend_url` | `string` | Link to explore this trend on Google Trends |
| `ai_marketing_intelligence` | `object` | AI-generated marketing intelligence insights for the trend |
| `ai_marketing_intelligence.why_it_matters` | `string` | Short description of the trend context or trigger (max 15 words) |
| `ai_marketing_intelligence.affected_sectors` | `string[]` | Relevant industry verticals (2-3 items) |
| `ai_marketing_intelligence.marketing_angle` | `string` | Tactical idea for newsjacking, editorial plan, or content creation |
| `ai_marketing_intelligence.paid_ads_advice` | `string` | Recommendation for Google Ads / Meta Ads |
| `ai_marketing_intelligence.brand_safety_risk` | `string` | Risk level for brand safety (`Low`, `Medium`, `High`) |

## Example Input

```json
{
  "AI_Marketing_Intelligence": true,
  "cat": "0",
  "geo": "IT",
  "hl": "it",
  "hours": "24",
  "max_items": 300,
  "sort": "search_volume",
  "status": "active"
}
```

## Output

Each trend is pushed as an individual record to the Apify Dataset, with `search_parameters` included:

```json
[
  {
    "title": "dancing with the stars",
    "search_volume": 500000,
    "growth_percentage": 1000,
    "started_at": 1789503000,
    "status": "active",
    "related_queries": [
      "dancing with the stars",
      "conner leavitt",
      "dwts",
      "dwts elimination",
      "dancing with the stars elimination",
      "who went home on dancing with the stars",
      "conner leavitt dancing with the stars",
      "dancing with the stars voting",
      "where to watch dancing with the stars",
      "julianne hough",
      "julia stiles",
      "dancing with the stars 2026 cast",
      "dancing with the stars 2026",
      "rylee arnold",
      "what time does dancing with the stars come on",
      "dancing with the stars season 35",
      "dwts vote",
      "dwts voting",
      "adele zaikman",
      "where can i watch dancing with the stars",
      "how to watch dancing with the stars",
      "whitney leavitt",
      "dancing with the stars cast",
      "who got voted off dancing with the stars tonight",
      "dwts cast",
      "dancing with the stars streaming",
      "when does dancing with the stars start",
      "dwts number",
      "dwts text number",
      "dancing with the stars vote",
      "connor leavitt",
      "dancing with the stars start date",
      "dancing with the stars time",
      "what is dancing with the stars on",
      "what time does dwts start",
      "dancing with the stars number",
      "dwts voting number",
      "when is dancing with the stars on",
      "ezra dancing with the stars",
      "abc dancing with the stars",
      "dancing with the stars premiere",
      "dancing with the stars text number",
      "who got eliminated from dancing with the stars",
      "what time is dwts on tonight",
      "what time is dwts",
      "what time is dancing with the stars on tonight",
      "amber glenn",
      "how long is dancing with the stars",
      "dancing with the stars voting number",
      "who got eliminated from dwts",
      "when does dwts start",
      "ezra dwts",
      "how to vote dancing with the stars text",
      "who went home on dwts",
      "what time does dancing with the stars start",
      "vote dancing with the stars",
      "how to vote for dancing with the stars",
      "what channel is dancing with the stars on",
      "dwts season 35",
      "who got eliminated on dancing with the stars",
      "dwts time",
      "dwts vote number",
      "how to vote dwts",
      "dancing with the stars live",
      "dwts premiere 2026",
      "dwts scores",
      "harry dancing with the stars",
      "who got eliminated from dwts tonight",
      "vote dwts",
      "how long is dwts tonight",
      "abc dwts vote",
      "connor dancing with the stars",
      "abc dwts",
      "abc dancing with the stars voting",
      "dancing with the stars time tonight",
      "dancing with the stars where to watch",
      "dancing with the stars text",
      "dancing with the stars cast 2026",
      "how to watch dancing with the stars live",
      "where to watch dwts live",
      "dancing with the stars voting app",
      "dwts vote online",
      "how to watch dwts live",
      "dancing with the stars start time",
      "dwts live",
      "jenna johnson dwts",
      "star"
    ],
    "category_ids": [
      4
    ],
    "trend_url": "https://trends.google.com/trends/explore?q=dancing+with+the+stars&geo=US",
    "search_parameters": {
      "geo": "US",
      "hl": "en",
      "hours": 24,
      "cat": 0,
      "sort": "search_volume",
      "status": "active"
    },
    "category_description": [
      "Entertainment"
    ],
    "ai_marketing_intelligence": {
      "why_it_matters": "High viewer engagement driven by weekly eliminations, voting queries, and cast announcements.",
      "affected_sectors": [
        "Entertainment",
        "Streaming Media",
        "Broadcasting"
      ],
      "marketing_angle": "Publish real-time elimination recaps and voting guides to capture high-intent search traffic.",
      "paid_ads_advice": "Increase bids on related show and voting queries during broadcast hours.",
      "brand_safety_risk": "Low"
    }
  },
  {
    "title": "eliana moreno",
    "search_volume": 200000,
    "growth_percentage": 1000,
    "started_at": 1789525800,
    "status": "active",
    "related_queries": [
      "eliana moreno",
      "helicopter crash",
      "eliana moreno nbc",
      "chatsworth",
      "la helicopter crash",
      "nbc helicopter crash",
      "knbc",
      "nbc helicopter",
      "helicopter",
      "news helicopter crash",
      "nbc news",
      "george marciniw",
      "chatsworth ca",
      "nbc4",
      "helicopter crash chatsworth",
      "news chopper 4",
      "nbc la",
      "helicopter crash la",
      "helicopter crash los angeles",
      "chatsworth helicopter",
      "ktla",
      "after",
      "knbc helicopter",
      "nbc los angeles",
      "eliana",
      "knbc helicopter crash",
      "knbc news",
      "chatsworth helicopter crash",
      "nbc4 los angeles",
      "nbcla",
      "knbc los angeles",
      "helicopter crash in chatsworth",
      "nbc 4",
      "colleen williams",
      "los angeles helicopter crash",
      "nbc4 helicopter",
      "nbc news helicopter crash",
      "la helicopter",
      "nbc 4 los angeles",
      "chatsworth crash",
      "ca",
      "in"
    ],
    "category_ids": [
      11
    ],
    "trend_url": "https://trends.google.com/trends/explore?q=eliana+moreno&geo=US",
    "search_parameters": {
      "geo": "US",
      "hl": "en",
      "hours": 24,
      "cat": 0,
      "sort": "search_volume",
      "status": "active"
    },
    "category_description": [
      "Other"
    ],
    "ai_marketing_intelligence": {
      "why_it_matters": "Breaking news search spike resulting from a tragic helicopter crash involving media personnel.",
      "affected_sectors": [
        "News and Media",
        "Publishing",
        "Broadcasting"
      ],
      "marketing_angle": "Provide accurate, respectful, and updated news coverage adhering to sensitive breaking news protocols.",
      "paid_ads_advice": "Add as negative keyword across non-news commercial campaigns to prevent association with tragedy.",
      "brand_safety_risk": "High"
    }
  }
]
```

## Error Handling

The Actor fails gracefully with descriptive messages for:

| Scenario | Behavior |
|----------|----------|
| HTTP 4xx/5xx errors | `Actor.fail()` with status code and response preview |
| Network timeout | `Actor.fail()` with timeout duration |
| Invalid JSON response | `Actor.fail()` with parse error details |

