# Indikátory: Jak je chápat a používat správně

- [Indikátory: Jak je chápat a používat správně](#indikátory-jak-je-chápat-a-používat-správně)
  - [🧠 1. **Co indikátory ve skutečnosti jsou**](#-1-co-indikátory-ve-skutečnosti-jsou)
  - [⚙️ 2. **Základní dělení indikátorů**](#️-2-základní-dělení-indikátorů)
  - [📊 3. **Jak indikátory používat smysluplně**](#-3-jak-indikátory-používat-smysluplně)
    - [Příklad:](#příklad)
  - [📈 4. **Typické chyby s indikátory**](#-4-typické-chyby-s-indikátory)
  - [📐 5. **Lagging vs. Leading indikátory**](#-5-lagging-vs-leading-indikátory)
  - [🧩 6. **Jak indikátor vybírat**](#-6-jak-indikátor-vybírat)
  - [🧪 7. **Testování indikátorů**](#-7-testování-indikátorů)
  - [📚 8. **Kde se naučit víc**](#-8-kde-se-naučit-víc)


## 🧠 1. **Co indikátory ve skutečnosti jsou**

Indikátor je **výpočet založený na historických datech** — typicky ceně (Open, High, Low, Close) a objemu (Volume).
Neví nic o budoucnosti, pouze **popisuje minulost** nebo **usnadňuje interpretaci trendu, volatility či momenta**.

💡 Jinými slovy:

> Indikátor neříká, co se *stane*, ale pomáhá ti lépe pochopit, co se *děje*.


## ⚙️ 2. **Základní dělení indikátorů**

| Kategorie                   | Co měří                      | Příklady                                | Typický účel                                   |
| --------------------------- | ---------------------------- | --------------------------------------- | ---------------------------------------------- |
| **Trendové**                | Směr a sílu trendu           | SMA, [EMA](EMA.md), MACD, ADX, Parabolic SAR      | Určování, jestli trh roste nebo klesá          |
| **Momentum / Oscilátory**   | Rychlost a sílu pohybu       | RSI, Stochastic, CCI, ROC               | Hledání překoupenosti/přeprodanosti            |
| **Volatilita**              | Proměnlivost ceny            | Bollinger Bands, ATR, Keltner Channels  | Určení velikosti pohybů, vhodné pro stop-lossy |
| **Objemové**                | Aktivitu účastníků           | OBV, Volume Profile, Accum/Distribution | Sleduje „sílu“ pohybu podle objemu             |
| **Statistické / Pokročilé** | Odchylky od normálu, průměru | Z-score, Linear Regression, z-skalování | Mean reversion, arbitrážní strategie           |


## 📊 3. **Jak indikátory používat smysluplně**

Zkušený trader ví, že indikátor **není signál sám o sobě**.
Měl by být:

* **součástí systému**, který kombinuje více pohledů (trend + volatilita + potvrzení objemu),
* **konzistentní** napříč časovými rámci,
* a hlavně **testovatelný** (kvantitativně).

### Příklad:

Místo:

> „RSI < 30 = kupuji“
> Správně bys měl říct:
> „Pokud RSI < 30 a cena se odrazí od supportu, zároveň roste objem, vstupuji do mean reversion obchodu s R:R = 2:1.“


## 📈 4. **Typické chyby s indikátory**

| Chyba                                | Proč je to problém                                                     |
| ------------------------------------ | ---------------------------------------------------------------------- |
| Používáš příliš mnoho indikátorů     | Dublují stejnou informaci (např. RSI a Stochastic měří obojí momentum) |
| Měníš indikátory podle pocitu        | Ztrácíš konzistenci a testovatelnost systému                           |
| Nepřizpůsobíš indikátory timeframe   | Parametry fungují jinak na 1h grafu než na denním                      |
| Ignoruješ zpoždění indikátorů        | Trendové indikátory vždy reagují *po* pohybu, ne před ním              |
| Bereš indikátor jako věšteckou kouli | Nikdy „nepředpovídá“ – jen vizualizuje data jinak                      |


## 📐 5. **Lagging vs. Leading indikátory**

| Typ                        | Co dělá                        | Příklad              | Poznámka                                        |
| -------------------------- | ------------------------------ | -------------------- | ----------------------------------------------- |
| **Lagging (opožděné)**     | Potvrzují trend po jeho vzniku | SMA, EMA, MACD       | Dobré pro sledování trendu, špatné pro vstupy   |
| **Leading (předbíhající)** | Naznačují možný obrat          | RSI, Stochastic, ROC | Dobré pro mean reversion, často falešné signály |

⚖️ Kombinace obou typů (např. EMA + RSI) bývá nejefektivnější.


## 🧩 6. **Jak indikátor vybírat**

Když přemýšlíš, který indikátor použít, zeptej se:

1. Co chci měřit? (trend, sílu, volatilitu, odchylku)
2. Na jakém timeframe?
3. Jak indikátor zapadá do mé strategie?
4. Lze ho jednoduše kvantitativně testovat?

💡 Např.:

* Trend-following → EMA + ADX
* Mean reversion → RSI + Bollinger Bands
* Breakout → Donchian Channels + ATR
* Momentum → Rate of Change + Ranking


## 🧪 7. **Testování indikátorů**

Používej backtesting:

* Python knihovny: `backtesting.py`, `backtrader`, `vectorbt`
* Metoda: testuj indikátor s definovanými pravidly (např. RSI<30 = long, RSI>70 = close)
* Sleduj: Winrate, Sharpe ratio, Max drawdown, Profit factor


## 📚 8. **Kde se naučit víc**

| Oblast                        | Doporučené zdroje                                            |
| ----------------------------- | ------------------------------------------------------------ |
| Technická analýza obecně      | *John Murphy – Technical Analysis of the Financial Markets*  |
| Kvantitativní přístup         | *Ernest Chan – Quantitative Trading*                         |
| Python implementace           | YouTube kanály: „QuantNomad“, „Part Time Larry“, „TradeCode“ |
| Interaktivní testy indikátorů | [TradingView.com](https://www.tradingview.com) → Pine Editor |
