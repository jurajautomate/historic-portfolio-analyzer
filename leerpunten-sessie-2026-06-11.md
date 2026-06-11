# Sessienotities 11 juni 2026 — vraag 2 t/m 5 (analyse.ipynb)

> **Let op:** dit zijn ruwe sessienotities — een feitelijke inventaris van wat er
> vandaag gebeurde en behandeld is, als grondstof voor je eigen reflectie.
> Herschrijf in eigen woorden voor je portfolio; niet letterlijk overnemen.

## Concepten behandeld

- **Annualiseren.** Gemiddeld dagrendement × 252 naar jaarrendement, maar
  standaarddeviatie × √252. Reden: bij onafhankelijke dagen tellen de
  *varianties* op, niet de standaarddeviaties; risico groeit met de wortel van
  de tijd omdat toevallige uitslagen elkaar deels uitwissen
  (dronkenmanswandeling: na 100 willekeurige stappen sta je typisch √100 = 10
  stappen van het beginpunt). Sluit aan op de normale verdeling en de
  68-95-99,7-regel uit blok 3.
- **Python-notatie.** `**` is machtsverheffen; `x ** 0.5` is een wortel.
  Alternatief: `math.sqrt()` voor wie het explicieter leesbaar wil.
- **Betekenislaag boven statistiek.** `.mean()` en `.std()` beschrijven *hoe*
  je rekent; "rendement" en "risico" zijn wat die getallen in deze context
  *betekenen*. Functienamen daarom vanuit de aanroeper benoemd
  (`geannualiseerde_mean` / `geannualiseerde_std`).
- **Max drawdown als risicogetal.** Niet hoe hard de koers dagelijks trilt
  (std), maar hoeveel procent je vanaf je piek kwijt was op het slechtste
  moment — het meest "voelbare" risicogetal.

## Pandas-operaties nieuw geleerd

- `(1 + daily_returns).cumprod()` — rendementsreeks naar waarde-ontwikkeling van €1
- `.cummax()` — lopende piek bijhouden
- `waarde / piek - 1` + `.min()` — drawdown-reeks en het diepste punt
- `.idxmin()` — de *datum* van het diepste punt (23 maart 2020, coronacrash)
- Boolean masking: `returns[returns[benchmark] < 0]` — conditioneel selecteren
- (Geruststelling onderweg: de NaN in de eerste rij van `pct_change()` wordt
  door `mean`/`std`/`cumprod` standaard overgeslagen.)

## Codekwaliteit-momenten (leerdoel 1)

- **Parameternaam `weighed` was vanuit de aanroeper fout** — de functie werkt
  op élke reeks dagrendementen en werd ook op IWDA aangeroepen. Zelfde les als
  `myTickers` → `tickers` uit Arthurs review van 10 juni: de naam beschrijft
  wat de functie nodig heeft, niet waar je hem het eerst voor gebruikt.
  Hernoemd naar `daily_returns`.
- **Kolomvolgorde-check.** yfinance sorteert kolommen alfabetisch (EMIM, IUSN,
  IWDA); de gewichten-lijst is impliciet aan die volgorde gekoppeld. Bewust
  gecontroleerd dat `[0.2, 0.2, 0.6]` klopt voor 60/20/20 IWDA/EMIM/IUSN.
  Fragiel punt — raakt aan de error-handling-ambitie uit de projectopzet.
- **Generalisatie ongevraagd toegepast (vraag 4):** `benchmark` als parameter
  in plaats van `'IWDA.AS'` hardcoden.
- **Functiecompositie (vraag 5):** `kengetallen()` stelt drie eigen functies
  samen tot één `tuple[float, float, float]` — de herbruikbare opzet uit het
  projectplan betaalde zich hier uit zoals voorspeld.
- Reproduceerbaarheidscheck: Restart & Run All als afsluiting (cellen waren
  kriskras gedraaid).

## Inhoudelijke bevindingen (vraag 2 t/m 5)

| | Rendement/jaar | Risico/jaar | Max drawdown |
|---|---|---|---|
| Naïef 1/3 elk | 11,1% | 16,3% | −35,2% |
| Mix 60/20/20 | 12,0% | 15,9% | −34,6% |
| 100% IWDA | 13,4% | 15,7% | −33,6% |

- Vraag 2: de mix verloor op rendement (−1,4 pp/jaar) én risico van 100% IWDA;
  het extra risico werd in deze periode niet beloond.
- Vraag 3: dieptepunt beide portefeuilles op 23 maart 2020; de mix zakte zelfs
  een fractie dieper — de spreiding beschermde niet op het moment dat het
  nodig was (gevolg van de 0,92-correlatie uit vraag 1).
- Vraag 4: op IWDA-daaldagen deed IUSN het gemiddeld slechter (−0,77%) dan
  IWDA zelf (−0,72%); EMIM een fractie beter (−0,66%). Geen buffer, maar extra
  aandelenrisico; echte demping moet uit een andere beleggingscategorie komen.
- Vraag 5: monotoon patroon — hoe meer gewicht naar EMIM/IUSN, hoe slechter
  alle drie de kengetallen. De 60/20/20-weging was beter dan naïef wegen, maar
  alleen doordat hij minder van de slecht presterende fondsen vasthield.
- Persoonlijke les: −35% vanaf de piek moet je kunnen uitzitten zonder panisch
  te verkopen.

## Werkwijze van deze sessie

Begeleide sessie (sparring met AI-tutor): uitleg en de op te zoeken operaties
aangereikt gekregen, alle code zelf getypt, alle antwoordblokken zelf
geformuleerd (met redactionele feedback per vraag). Past binnen het
projectplan-principe: "bij langer dan 30 minuten vastlopen gericht hulp vragen
in plaats van eindeloos doorzoeken." Vermeld dit eerlijk zo in het portfolio.

Nog open: eindfeedback Arthur (feedbackmoment 2, placeholder `[INVULLEN NA
VANAVOND]` in het leerdoelen-doc).
