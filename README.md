# Google Trending Now

An Apify Actor that fetches real-time Google Trends data and saves the results to an Apify Dataset.

## What does this Actor do?

This Actor:
1. Accepts configurable parameters (country, language, time window, category, sort order, status)
2. Fetches the latest trending searches from Google Trends
3. Returns structured data including titles, search volumes, growth percentages, and related queries

Perfect for trend monitoring, content strategy, SEO research, market analysis, and real-time search intelligence.

## Why use Google Trending Now?

- **Real-time data** — Access the latest Google Trends data as it happens
- **Flexible filtering** — Filter by country, language, time window, category, and status
- **Multiple sort options** — Sort by relevance, search volume, recency, or title
- **Two output modes** — Get the full response or flattened records for easy table viewing
- **20 category filters** — From Sports and Technology to Politics and Climate
- **Production-ready** — Clean error handling with descriptive failure messages

## Input Schema

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `geo` | string | No | `"US"` | Two-letter country code (see table below) |
| `hl` | string | No | `"en"` | Language code (e.g. `en`, `it`, `es`, `de`) |
| `hours` | integer | No | `24` | Time window. Options: `4`, `24`, `48`, `168` |
| `cat` | integer | No | `0` | Category ID filter (see table below) |
| `sort` | string | No | `"relevance"` | Sort order: `relevance`, `search_volume`, `recency`, `title` |
| `status` | string | No | `"all"` | Trend status filter: `all`, `active` |
| `flattenTrends` | boolean | No | `false` | If `true`, pushes each trend as an individual Dataset record |

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

| Country Code | Description |
| :--- | :--- |
| AD | Andorra |
| AE | United Arab Emirates |
| AF | Afghanistan |
| AG | Antigua and Barbuda |
| AI | Anguilla |
| AL | Albania |
| AM | Armenia |
| AO | Angola |
| AQ | Antarctica |
| AR | Argentina |
| AS | American Samoa |
| AT | Austria |
| AU | Australia |
| AW | Aruba |
| AX | Åland Islands |
| AZ | Azerbaijan |
| BA | Bosnia and Herzegovina |
| BB | Barbados |
| BD | Bangladesh |
| BE | Belgium |
| BF | Burkina Faso |
| BG | Bulgaria |
| BH | Bahrain |
| BI | Burundi |
| BJ | Benin |
| BL | Saint Barthélemy |
| BM | Bermuda |
| BN | Brunei Darussalam |
| BO | Bolivia |
| BQ | Bonaire, Sint Eustatius and Saba |
| BR | Brazil |
| BS | Bahamas |
| BT | Bhutan |
| BV | Bouvet Island |
| BW | Botswana |
| BY | Belarus |
| BZ | Belize |
| CA | Canada |
| CC | Cocos (Keeling) Islands |
| CD | Democratic Republic of the Congo |
| CF | Central African Republic |
| CG | Republic of the Congo |
| CH | Switzerland |
| CI | Côte d'Ivoire |
| CK | Cook Islands |
| CL | Chile |
| CM | Cameroon |
| CN | China |
| CO | Colombia |
| CR | Costa Rica |
| CU | Cuba |
| CV | Cabo Verde |
| CW | Curaçao |
| CX | Christmas Island |
| CY | Cyprus |
| CZ | Czechia |
| DE | Germany |
| DJ | Djibouti |
| DK | Denmark |
| DM | Dominica |
| DO | Dominican Republic |
| DZ | Algeria |
| EC | Ecuador |
| EE | Estonia |
| EG | Egypt |
| EH | Western Sahara |
| ER | Eritrea |
| ES | Spain |
| ET | Ethiopia |
| FI | Finland |
| FJ | Fiji |
| FK | Falkland Islands |
| FM | Micronesia |
| FO | Faroe Islands |
| FR | France |
| GA | Gabon |
| GB | United Kingdom |
| GD | Grenada |
| GE | Georgia |
| GF | French Guiana |
| GG | Guernsey |
| GH | Ghana |
| GI | Gibraltar |
| GL | Greenland |
| GM | Gambia |
| GN | Guinea |
| GP | Guadeloupe |
| GQ | Equatorial Guinea |
| GR | Greece |
| GS | South Georgia and the South Sandwich Islands |
| GT | Guatemala |
| GU | Guam |
| GW | Guinea-Bissau |
| GY | Guyana |
| HK | Hong Kong |
| HM | Heard Island and McDonald Islands |
| HN | Honduras |
| HR | Croatia |
| HT | Haiti |
| HU | Hungary |
| ID | Indonesia |
| IE | Ireland |
| IL | Israel |
| IM | Isle of Man |
| IN | India |
| IO | British Indian Ocean Territory |
| IQ | Iraq |
| IR | Iran |
| IS | Iceland |
| IT | Italy |
| JE | Jersey |
| JM | Jamaica |
| JO | Jordan |
| JP | Japan |
| KE | Kenya |
| KG | Kyrgyzstan |
| KH | Cambodia |
| KI | Kiribati |
| KM | Comoros |
| KN | Saint Kitts and Nevis |
| KP | North Korea |
| KR | South Korea |
| KW | Kuwait |
| KY | Cayman Islands |
| KZ | Kazakhstan |
| LA | Laos |
| LB | Lebanon |
| LC | Saint Lucia |
| LI | Liechtenstein |
| LK | Sri Lanka |
| LR | Liberia |
| LS | Lesotho |
| LT | Lithuania |
| LU | Luxembourg |
| LV | Latvia |
| LY | Libya |
| MA | Morocco |
| MC | Monaco |
| MD | Moldova |
| ME | Montenegro |
| MF | Saint Martin |
| MG | Madagascar |
| MH | Marshall Islands |
| MK | North Macedonia |
| ML | Mali |
| MM | Myanmar |
| MN | Mongolia |
| MO | Macao |
| MP | Northern Mariana Islands |
| MQ | Martinique |
| MR | Mauritania |
| MS | Montserrat |
| MT | Malta |
| MU | Mauritius |
| MV | Maldives |
| MW | Malawi |
| MX | Mexico |
| MY | Malaysia |
| MZ | Mozambique |
| NA | Namibia |
| NC | New Caledonia |
| NE | Niger |
| NF | Norfolk Island |
| NG | Nigeria |
| NI | Nicaragua |
| NL | Netherlands |
| NO | Norway |
| NP | Nepal |
| NR | Nauru |
| NU | Niue |
| NZ | New Zealand |
| OM | Oman |
| PA | Panama |
| PE | Peru |
| PF | French Polynesia |
| PG | Papua New Guinea |
| PH | Philippines |
| PK | Pakistan |
| PL | Poland |
| PM | Saint Pierre and Miquelon |
| PN | Pitcairn |
| PR | Puerto Rico |
| PS | Palestine |
| PT | Portugal |
| PW | Palau |
| PY | Paraguay |
| QA | Qatar |
| RE | Réunion |
| RO | Romania |
| RS | Serbia |
| RU | Russia |
| RW | Rwanda |
| SA | Saudi Arabia |
| SB | Solomon Islands |
| SC | Seychelles |
| SD | Sudan |
| SE | Sweden |
| SG | Singapore |
| SH | Saint Helena, Ascension and Tristan da Cunha |
| SI | Slovenia |
| SJ | Svalbard and Jan Mayen |
| SK | Slovakia |
| SL | Sierra Leone |
| SM | San Marino |
| SN | Senegal |
| SO | Somalia |
| SR | Suriname |
| SS | South Sudan |
| ST | Sao Tome and Principe |
| SV | El Salvador |
| SX | Sint Maarten |
| SY | Syria |
| SZ | Eswatini |
| TC | Turks and Caicos Islands |
| TD | Chad |
| TF | French Southern Territories |
| TG | Togo |
| TH | Thailand |
| TJ | Tajikistan |
| TK | Tokelau |
| TL | Timor-Leste |
| TM | Turkmenistan |
| TN | Tunisia |
| TO | Tonga |
| TR | Türkiye |
| TT | Trinidad and Tobago |
| TV | Tuvalu |
| TW | Taiwan |
| TZ | Tanzania |
| UA | Ukraine |
| UG | Uganda |
| UM | United States Minor Outlying Islands |
| US | United States |
| UY | Uruguay |
| UZ | Uzbekistan |
| VA | Holy See |
| VC | Saint Vincent and the Grenadines |
| VE | Venezuela |
| VG | Virgin Islands (British) |
| VI | Virgin Islands (U.S.) |
| VN | Viet Nam |
| VU | Vanuatu |
| WF | Wallis and Futuna |
| WS | Samoa |
| YE | Yemen |
| YT | Mayotte |
| ZA | South Africa |
| ZM | Zambia |
| ZW | Zimbabwe |

### Language Code

| Language Code | Description |
| :--- | :--- |
| aa | Afar |
| ab | Abkhazian |
| af | Afrikaans |
| am | Amharic |
| ar | Arabic |
| as | Assamese |
| ay | Aymara |
| az | Azerbaijani |
| ba | Bashkir |
| be | Belarusian |
| bg | Bulgarian |
| bh | Bihari |
| bi | Bislama |
| bn | Bengali |
| bo | Tibetan |
| br | Breton |
| ca | Catalan |
| co | Corsican |
| cs | Czech |
| cy | Welsh |
| da | Danish |
| de | German |
| dz | Bhutani |
| el | Greek |
| en | English |
| eo | Esperanto |
| es | Spanish |
| et | Estonian |
| eu | Basque |
| fa | Persian |
| fi | Finnish |
| fj | Fiji |
| fo | Faroese |
| fr | French |
| fy | Frisian |
| ga | Irish |
| gd | Scots Gaelic |
| gl | Galician |
| gn | Guarani |
| gu | Gujarati |
| ha | Hausa |
| he | Hebrew |
| hi | Hindi |
| hr | Croatian |
| hu | Hungarian |
| hy | Armenian |
| ia | Interlingua |
| id | Indonesian |
| ie | Interlingue |
| ik | Inupiak |
| is | Icelandic |
| it | Italian |
| iu | Inuktitut |
| ja | Japanese |
| jw | Javanese |
| ka | Georgian |
| kk | Kazakh |
| kl | Greenlandic |
| km | Cambodian |
| kn | Kannada |
| ko | Korean |
| ks | Kashmiri |
| ku | Kurdish |
| ky | Kirghiz |
| la | Latin |
| ln | Lingala |
| lo | Laothian |
| lt | Lithuanian |
| lv | Latvian |
| mg | Malagasy |
| mi | Maori |
| mk | Macedonian |
| ml | Malayalam |
| mn | Mongolian |
| mo | Moldavian |
| mr | Marathi |
| ms | Malay |
| mt | Maltese |
| my | Burmese |
| na | Nauru |
| ne | Nepali |
| nl | Dutch |
| no | Norwegian |
| oc | Occitan |
| om | Oromo |
| or | Oriya |
| pa | Punjabi |
| pl | Polish |
| ps | Pashto |
| pt | Portuguese |
| qu | Quechua |
| rm | Rhaeto-Romance |
| rn | Kirundi |
| ro | Romanian |
| ru | Russian |
| rw | Kinyarwanda |
| sa | Sanskrit |
| sd | Sindhi |
| sg | Sangro |
| sh | Serbo-Croatian |
| si | Singhalese |
| sk | Slovak |
| sl | Slovenian |
| sm | Samoan |
| sn | Shona |
| so | Somali |
| sq | Albanian |
| sr | Serbian |
| ss | Siswati |
| st | Sesotho |
| su | Sundanese |
| sv | Swedish |
| sw | Swahili |
| ta | Tamil |
| te | Telugu |
| tg | Tajik |
| th | Thai |
| ti | Tigrinya |
| tk | Turkmen |
| tl | Tagalog |
| tn | Setswana |
| to | Tonga |
| tr | Turkish |
| ts | Tsonga |
| tt | Tatar |
| tw | Twi |
| ug | Uighur |
| uk | Ukrainian |
| ur | Urdu |
| uz | Uzbek |
| vi | Vietnamese |
| vo | Volapuk |
| wo | Wolof |
| xh | Xhosa |
| yi | Yiddish |
| yo | Yoruba |
| za | Zhuang |
| zh | Chinese |
| zu | Zulu |

## Output

Each trend is pushed as an individual record to the Apify Dataset, with `search_parameters` included:

```json
{
  "title": "Example Trend",
  "search_volume": 200000,
  "growth_percentage": 1000,
  "started_at": 1775782200,
  "status": "active",
  "related_queries": ["query 1", "query 2"],
  "category_ids": [17],
  "trend_url": "https://trends.google.com/...",
  "search_parameters": {
    "geo": "US",
    "hl": "en",
    "hours": 24,
    "cat": 0,
    "sort": "relevance",
    "status": "all"
  }
}
```

## Example Input

```json
{
  "geo": "IT",
  "hl": "it",
  "hours": 24,
  "cat": 0,
  "sort": "search_volume",
  "status": "active"
}
```

## Error Handling

The Actor fails gracefully with descriptive messages for:

| Scenario | Behavior |
|----------|----------|
| Missing `SCRAPEDO_TOKEN` env var | `Actor.fail()` with clear instructions |
| HTTP 4xx/5xx errors | `Actor.fail()` with status code and response preview |
| Network timeout | `Actor.fail()` with timeout duration |
| Invalid JSON response | `Actor.fail()` with parse error details |

## Technology

- **Runtime**: Python 3.14 on Apify Docker image
- **HTTP Client**: `httpx` (async)
- **SDK**: `apify` Python SDK
