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
| `geo` | string | Yes | `"US"` | Two-letter country code (see table below) |
| `hl` | string | No | `"en"` | Language code (e.g. `en`, `it`, `es`, `de`, ... see table below) |
| `hours` | integer | No | `24` | Time window. Options: `4`, `24`, `48`, `168` |
| `cat` | integer | No | `0` | Category ID filter (see table below) |
| `sort` | string | No | `"relevance"` | Sort order: `relevance`, `search_volume`, `recency`, `title` |
| `status` | string | No | `"all"` | Trend status filter: `all`, `active` |
| `max_items` | integer | No | `2000` | Maximum number of trending items to return |

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


## Example Input

```json
{
    "cat": "0",
    "geo": "US",
    "hl": "en",
    "hours": "168",
    "max_items": 3,
    "sort": "search_volume",
    "status": "all"
}
```

## Output

Each trend is pushed as an individual record to the Apify Dataset, with `search_parameters` included:

```json
[
  {
    "title": "tim curry",
    "search_volume": 5000000,
    "growth_percentage": 1000,
    "started_at": 1787757000,
    "status": "active",
    "related_queries": [
      "tim curry",
      "rocky horror picture show",
      "tim curry movies",
      "tim curry died",
      "was tim curry gay",
      "rocky horror",
      "tim.curry",
      "tim curry movies and tv shows",
      "home alone",
      "tim curry death",
      "tim curry cause of death",
      "tim curry stroke",
      "tom curry",
      "tim curry home alone",
      "home alone 2",
      "how did tim curry die",
      "jim curry",
      "home alone cast",
      "clue movie",
      "who is tim curry",
      "when did tim curry die",
      "clue",
      "home alone 2 cast",
      "the rocky horror picture show",
      "did tim curry die",
      "tim curry gay",
      "tim",
      "tim curry dead",
      "tim curry wife",
      "nigel thornberry",
      "tim curry home alone 2",
      "tim curry rocky horror",
      "tim curry age",
      "tim curry pennywise",
      "dr frank n furter",
      "susan sarandon",
      "tim curry criminal minds",
      "tim curry legend",
      "tim curry clue",
      "frank n furter",
      "legend",
      "what did tim curry die of",
      "tim curry imdb",
      "tom curry actor",
      "tm curry",
      "was tim curry ever married",
      "timmy curry",
      "lesley ann warren",
      "tim. curry",
      "muppet treasure island",
      "tim curry death cause",
      "did tim curry really die",
      "legend 1985",
      "time curry",
      "is tim curry still alive",
      "tim curry.",
      "pennywise actor",
      "tim curry actor",
      "tim carry",
      "tim curry net worth",
      "home alone 2 tim curry",
      "luke evans",
      "did tim curry pass away",
      "actor tim curry passing",
      "tim curry los feliz home sale",
      "tim curry how did he die",
      "actor tim curry",
      "is tim curry dead",
      "tim.curry movies",
      "is tim curry still alive?",
      "tim curru",
      "actor died today",
      "brutal legend",
      "tim curry and dolly parton",
      "tim curry die",
      "what celebrity died today",
      "tim curry dies",
      "tim curry movie",
      "tim curry alive",
      "how old was tim curry",
      "tim curry passed away",
      "tim curry now",
      "legend tim curry",
      "was tim curry in home alone",
      "tim curry rocky horror picture show",
      "tim curry filmography",
      "tim curry films",
      "tim death",
      "tim curry in home alone",
      "where to watch rocky horror picture show",
      "did tim curry die?",
      "tim curry news",
      "tim curry dead?",
      "tim curry space",
      "what did tim curry die from",
      "tom curry movies",
      "tim curry died?",
      "rim curry",
      "tim curry career and roles",
      "tim.curry now",
      "tim curry passed",
      "tim died",
      "tim curry passing",
      "did tim curry die today",
      "did tim curry pass away?",
      "whos tim curry",
      "how did tim curry pass away",
      "who was tim curry",
      "when did tim curry pass away",
      "tim curry muppets",
      "tim curry 2026",
      "tim curry passing at 80",
      "celebrity deaths today",
      "tom.curry",
      "tim curry illness",
      "ti curry",
      "has tim curry died",
      "bbc news tim curry",
      "home alone tim curry",
      "what happened to tim curry",
      "tim curry movies and shows",
      "tim curry in home alone 2",
      "tim curry tmz",
      "who died",
      "tim curry partner",
      "tim.curry death",
      "tim curry die?",
      "tim curry voice acting",
      "when did tim curry pass",
      "tim curry health",
      "tim curry disease",
      "pennywise tim curry",
      "rip tim curry",
      "tim curry nyt",
      "tim curry frank n furter",
      "tim curry desth",
      "what did tim curry play in",
      "british actor tim curry passing",
      "ti. curry",
      "tim curry death date",
      "tim curry -ai",
      "actor who died today",
      "tim curry shows",
      "tim curry command and conquer",
      "tim curry dead or alive",
      "tim curry did he die",
      "jaye p morgan home alone",
      "tim curry red alert",
      "how old is tim curry",
      "tmz tim curry",
      "tim dead",
      "tim curry died 2026"
    ],
    "category_ids": [
      4
    ],
    "trend_url": "https://trends.google.com/trends/explore?q=tim+curry&geo=US",
    "search_parameters": {
      "geo": "US",
      "hl": "en",
      "hours": 168,
      "cat": 0,
      "sort": "search_volume",
      "status": "all"
    },
    "category_description": [
      "Entertainment"
    ]
  },
  {
    "title": "peter cullen",
    "search_volume": 2000000,
    "growth_percentage": 1000,
    "started_at": 1787815200,
    "status": "active",
    "related_queries": [
      "peter cullen",
      "transformers",
      "optimus prime",
      "optimus prime voice",
      "peter cullen movies",
      "transformers optimus prime awakening",
      "peter cullen dead",
      "eeyore",
      "voice of optimus prime",
      "transformers movies",
      "winnie the pooh",
      "celebrity deaths this week",
      "optimus prime voice actor",
      "eeyore voice actor",
      "optimus prime death",
      "peter cullen death",
      "did peter cullen die",
      "peter cullen cause of death",
      "who died yesterday",
      "peter cullen voices",
      "peter cullen invincible",
      "peter cullen movies and tv shows",
      "optimus prime voice actor died",
      "voice of eeyore",
      "how did peter cullen die",
      "when did peter cullen die",
      "transformers voice actor peter cullen passes",
      "voice actor for optimus prime",
      "who voiced optimus prime",
      "petter cullen",
      "peter cullen age",
      "what actor died today",
      "invincible",
      "who is peter cullen",
      "peter cullen eeyore",
      "optimus prime actor",
      "peter cullen optimus prime",
      "is peter cullen still alive",
      "pete cullen",
      "peter cullen winnie the pooh",
      "optimus prime dead",
      "optimus",
      "is peter cullen dead",
      "optimus prime voice actors",
      "cullen",
      "peter",
      "who passed away today",
      "optimus prime died",
      "eeyore from winnie the pooh",
      "peter cullen transformers",
      "peter.cullen",
      "peter cullen imdb",
      "the voice of optimus prime",
      "voice actor of optimus prime",
      "perer cullen",
      "who voices optimus prime"
    ],
    "category_ids": [
      4
    ],
    "trend_url": "https://trends.google.com/trends/explore?q=peter+cullen&geo=US",
    "search_parameters": {
      "geo": "US",
      "hl": "en",
      "hours": 168,
      "cat": 0,
      "sort": "search_volume",
      "status": "all"
    },
    "category_description": [
      "Entertainment"
    ]
  },
  {
    "title": "lindsay clancy",
    "search_volume": 1000000,
    "growth_percentage": 100,
    "started_at": 1787851800,
    "ended_at": 1787967600,
    "status": "ended",
    "related_queries": [
      "lindsay clancy",
      "verdict lindsay clancy",
      "lindsay clancy update",
      "clancy trial verdict",
      "what happens if there's a hung jury",
      "clancy",
      "lindsay clancy live trial today",
      "clancy trial live",
      "lindsey clancy",
      "clancy trial update",
      "clancy trial",
      "what does deadlock jury mean",
      "lindsay clancy closing arguments",
      "what does a hung jury mean",
      "is there a verdict in the lindsay clancy case",
      "lindsay clancy trial live",
      "lindsey clancy verdict",
      "court tv live",
      "lindsey clancy trial updates",
      "tuey rodriguez instructions",
      "lindsay clancey",
      "deadlocked",
      "what happens when there is a hung jury",
      "what is a deadlocked jury",
      "what happens if a jury is deadlocked",
      "deadlock jury",
      "what happens in a hung jury",
      "lindsay clancy verdict yet",
      "lindsay clancy jury deliberation",
      "why is lindsay clancy in a wheelchair",
      "lindsay clancy trial verdict",
      "deadlocked jury meaning",
      "what does hung jury mean",
      "what does deadlocked jury mean",
      "lyndsay clancy",
      "hung jury what happens",
      "clancy jury",
      "lindsay clancy jury",
      "karen read",
      "lindsay clancy trial update",
      "jury deadlock meaning",
      "why is lindsay clancy in a wheelchair in the courtroom",
      "lindsay clancy verdict notification",
      "what does it mean when a jury is deadlocked",
      "lindsay clancy verdict day",
      "clancy trial verdict update",
      "clancy trial closing arguments",
      "what happens if jury cant reach a verdict",
      "what happens if a jury cant reach a verdict",
      "clancy trial live today",
      "lindsay clancy verdict options",
      "lindsay clancy trial live today",
      "lindsey clancy trial live",
      "what happens when a jury is deadlocked",
      "lindsay clancy verdict update",
      "lindsay clancy final results",
      "lindsay clancy live updates",
      "clancy trial today",
      "who is lindsay clancy",
      "what does a deadlocked jury mean",
      "what is deadlocked jury",
      "lindsay clancy case",
      "what is a hung jury mean",
      "deadlock jury meaning",
      "what happens if there is a hung jury",
      "lindsey clancy trial",
      "what does a deadlock jury mean",
      "kevin reddington",
      "psychiatrist",
      "closing arguments for lindsay clancy",
      "bowden charge",
      "lindsay clancy hung jury",
      "bowden instruction",
      "what happens if a jury is hung",
      "lindsay clancy live",
      "lindsay clancy verdict odds",
      "clancy verdict update",
      "lindsay clancey verdict",
      "clancy trial recap",
      "court tv live stream",
      "lindsey clancy trial update",
      "lindsay clancy trial live day 22",
      "jennifer sprague",
      "lindsay clancy husband",
      "lindsay clancy verdict jury",
      "susan smith",
      "lindsay clancy trial live updates",
      "lindsay clancy trial day 21",
      "lindsay clancy paralyzed",
      "lindsay clancy trial live day 21",
      "lindsay clancy day 21",
      "lindsey clancy trial today",
      "what time does the lindsay clancy trial resume today",
      "live lindsay clancy trial",
      "verdict on lindsay clancy",
      "what did lindsay clancy do"
    ],
    "category_ids": [
      10
    ],
    "trend_url": "https://trends.google.com/trends/explore?q=lindsay+clancy&geo=US",
    "search_parameters": {
      "geo": "US",
      "hl": "en",
      "hours": 168,
      "cat": 0,
      "sort": "search_volume",
      "status": "all"
    },
    "category_description": [
      "Law and Government"
    ]
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

