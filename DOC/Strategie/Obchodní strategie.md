# Obchodní strategie pro algoritmické obchodování
- [Obchodní strategie pro algoritmické obchodování](#obchodní-strategie-pro-algoritmické-obchodování)
  - [📘 Doporučené obecné zdroje pro všechny typy](#-doporučené-obecné-zdroje-pro-všechny-typy)
  - [Typy obchodních strategií](#typy-obchodních-strategií)
    - [🧭 Trend-Following (sledování trendu)](#-trend-following-sledování-trendu)
    - [⚖️ Mean Reversion (návrat k průměru)](#️-mean-reversion-návrat-k-průměru)
    - [💥 Breakout strategie (proražení hranice)](#-breakout-strategie-proražení-hranice)
    - [📊 Momentum strategie](#-momentum-strategie)
    - [💹 Arbitrážní a párové strategie (Pairs Trading, Stat Arb)](#-arbitrážní-a-párové-strategie-pairs-trading-stat-arb)
    - [⚙️ Market Making \& High-Frequency strategie](#️-market-making--high-frequency-strategie)
  - [📊 Přehled obchodovatelných strategií](#-přehled-obchodovatelných-strategií)
    - [Význam sloupců (metrik):](#význam-sloupců-metrik)


## 📘 Doporučené obecné zdroje pro všechny typy

| Typ             | Kniha / Autor                                      | Web / Kurz                                                   |
| --------------- | ----------------------- | --------------------------------- |
| Trend-Following | Michael Covel                        | [trendfollowing.com](https://www.trendfollowing.com)                             |
| Mean Reversion  | Ernest Chan                                        | [quantstart.com](https://www.quantstart.com)                                               |
| Breakout        | Toby Crabel                                        | [Linda Raschke YT](https://www.youtube.com/results?search_query=linda+raschke)                                             |
| Momentum        | Andreas Clenow                                     | [quantinsti.com](https://www.quantinsti.com)                                               |
| Stat Arb        | Ernest Chan                                        | [quantopian tutorials](https://www.quantopian.com/tutorials)                                         |
| Všeobecně       | Marcos López de Prado – *Advances in Financial ML* | [coursera.org](https://www.coursera.org) – “Machine Learning for Trading” (Georgia Tech) |

| Kategorie                 | Doporučené knihy / autoři                                                                   | Online zdroje                                  |
| ------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Trend / Momentum          | *Michael Covel – Trend Following*, *Andreas Clenow – Stocks on the Move*                    | trendfollowing.com, QuantInsti Momentum Course |
| Mean Reversion / Stat Arb | *Ernest Chan – Quantitative Trading*, *Algorithmic Trading*                                 | quantstart.com, quantinsti.com                 |
| Breakout / Discretionary  | *Toby Crabel – Day Trading with Short-Term Price Patterns*, *Linda Raschke – Street Smarts* | YouTube: “Breakout backtesting Backtrader”     |
| Portfolio & Risk Mgmt     | *Marcos López de Prado – Advances in Financial Machine Learning*                            | coursera.org → “Machine Learning for Trading”  |
| Market Microstructure     | *Larry Harris – Trading and Exchanges*, *Cartea & Jaimungal – HFT*                          | medium.com/topic/algo-trading                  |

## Typy obchodních strategií

### 🧭 Trend-Following (sledování trendu)

**Myšlenka:**

> „Trend is your friend.“ — cena má tendenci se pohybovat v trendech, a tak je výhodné se k nim přidat, ne proti nim.

**Jak to funguje:**

* Vstupuješ, když cena potvrzuje trend (např. prorazí klíčovou úroveň nebo klouzavý průměr).
* Výstupuješ, když trend oslabuje (např. křížení klouzavých průměrů opačným směrem).
* Cílem není chytit dno/vrchol, ale většinu trendového pohybu.

**Příklady indikátorů:**

* Moving Average Crossovers (SMA, EMA)
* ADX (Average Directional Index)
* Donchian Channels
* Parabolic SAR

**Typické trhy:** komodity, měny, akcie, futures

**Timeframes:** denní až týdenní

> [!warning] Problém:
> nízká úspěšnost (např. 30–40 %), ale velké zisky z vítězných obchodů.

**Kde se naučit víc:**

* 📘 *Michael Covel – Trend Following*
* 🧠 Turtle Traders story (Richard Dennis experiment)
* Web: [https://www.trendfollowing.com](https://www.trendfollowing.com)


### ⚖️ Mean Reversion (návrat k průměru)

**Myšlenka:**

> Ceny se mají tendenci vracet ke své „spravedlivé“ hodnotě po odchýlení.

**Jak to funguje:**

* Když cena „uteče“ příliš vysoko (např. nad klouzavý průměr nebo statistický průměr), očekáváš návrat dolů.
* Když je příliš nízko, očekáváš návrat nahoru.
* Funguje nejlépe v „range-bound“ trzích (kde se cena pohybuje v pásmu).

**Indikátory:**

* Bollinger Bands
* RSI (překoupenost/přeprodanost)
* Z-score z klouzavého průměru
* Pairs trading (statistická arbitráž)

**Výhoda:** časté malé zisky

> [!warning] Nevýhoda:
> V silném trendu může utrpět velkou ztrátu (proto musí být řízení rizika přísné).

**Kde se učit:**

* *Ernest Chan – Quantitative Trading* (praktické ukázky mean reversion strategií)
* *Marcos López de Prado – Advances in Financial Machine Learning* (statistická verze)
* Web: [QuantStart.com](https://www.quantstart.com), [QuantInsti.com](https://www.quantinsti.com)


### 💥 Breakout strategie (proražení hranice)

**Myšlenka:**

> Když cena prorazí důležitou úroveň (support/resistance, maximum/minimum), může pokračovat dál — často po akumulaci objemu.

**Jak to funguje:**

* Sleduješ konsolidaci (např. úzké pásmo nebo trojúhelník).
* Po proražení nastavíš vstup stejným směrem.
* Používá se i na objemových datech — pokud breakout doprovází růst objemu, je „validní“.

**Indikátory / techniky:**

* Donchian Channels (např. 20-day breakout)
* Bollinger Band squeeze
* Range breakouts (např. první hodina dne)
* Volume profile / VWAP

**Typicky:** intradenní nebo krátkodobé obchodování

> [!warning] Problém:
> falešné breakouts — často nutná filtrace podle volatility nebo objemu.

**Kde se učit:**

* *Toby Crabel – Day Trading with Short Term Price Patterns and Opening Range Breakout*
* *Linda Bradford Raschke – Street Smarts*
* YouTube: „Breakout strategy backtest“ + Backtrader tutorials


### 📊 Momentum strategie

**Myšlenka:**

> Akcie, které se chovaly dobře v minulosti, mají tendenci být výkonné i v budoucnu (krátkodobě až střednědobě).

**Jak to funguje:**

* Třídíš akcie podle výkonu za poslední období (např. 3 nebo 6 měsíců).
* Nakupuješ nejsilnější, shortuješ nejslabší.
* Obnovuješ portfolio periodicky.

**Používá se v:** kvantitativních fondech (AQR, Two Sigma apod.)
**Vyžaduje:** velký dataset a portfoliový přístup.

**Kde se učit:**

* *Jegadeesh & Titman (1993): Returns to Buying Winners and Selling Losers*
* *Andreas Clenow – Stocks on the Move*
* Quantopian/Zipline tutorials (pro Python)


### 💹 Arbitrážní a párové strategie (Pairs Trading, Stat Arb)

**Myšlenka:**

> Dvě ceny (např. akcií, ETF nebo futures) jsou historicky korelované. Pokud se jejich spread odchýlí, vsadím na návrat ke korelaci.

**Příklad:**

* Coca-Cola vs Pepsi — pokud se jeden pohne výrazně jinak, obchodník shortuje jeden a longuje druhý.

**Používá se v:** hedge fondech, high-frequency trading
**Nástroje:** korelace, cointegrace, z-score, PCA

**Kde se učit:**

* *Ernest Chan – Algorithmic Trading*
* *A Practical Guide to Quantitative Finance Interviews* (příklady cointegrace)
* Web: *QuantInsti – Pairs Trading Guide*


### ⚙️ Market Making & High-Frequency strategie

**Myšlenka:**

> Poskytuješ likviditu — dáváš nabídky (bid) a poptávky (ask) a vyděláváš na rozdílu (spreadu).

Vyžaduje:

* Přístup na nízko-latenční infrastrukturu
* API přímo k burze
* Statistické modely odhadu volatility a order flow

Pro retail tradera spíše **teoretické**, ale dobré pro pochopení mikrostruktury trhu.

**Kde se učit:**

* *Larry Harris – Trading and Exchanges*
* *Cartea, Jaimungal – Algorithmic and High-Frequency Trading*


## 📊 Přehled obchodovatelných strategií

| Typ strategie                            | Hlavní princip                                 | Typické indikátory / přístupy                           | Vhodné trhy           | Typický timeframe  | Winrate | Risk/Reward    | Výhody                                          | Nevýhody                                   |
| ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------- | --------------------- | ------------------ | ------- | -------------- | ----------------------------------------------- | ------------------------------------------ |
| **Trend-Following**                      | Sledování silných trendů a přidání se k nim    | MA Cross, ADX, Donchian Channels, MACD                  | Komodity, měny, akcie | Denní – týdenní    | 30–45 % | 2–5 : 1        | Velké zisky při dlouhých trendech, jednoduchost | Dlouhá období ztrát v netrendových trzích  |
| **Mean Reversion**                       | Cena se vrací ke svému průměru                 | RSI, Bollinger Bands, Z-score, SMA deviation            | Akcie, ETF, indexy    | Intradenní – denní | 60–75 % | 1 : 1 až 1 : 2 | Časté malé zisky, stabilní equity               | Katastrofické ztráty při silném trendu     |
| **Breakout**                             | Vstup po proražení důležité úrovně             | Donchian Channels, Bollinger squeeze, Volume spike      | Akcie, futures, forex | Intradenní – denní | 35–55 % | 2–3 : 1        | Možnost velkých pohybů, jednoduchý systém       | Falešné breakouts, potřeba filtrace objemu |
| **Momentum**                             | „Silné akcie zůstávají silné“                  | Rate of Change, Relative Strength, ranking podle výkonu | Akcie, ETF            | Denní – měsíční    | 45–60 % | 1.5–3 : 1      | Dobře funguje ve střednědobém horizontu         | Kolaps po změně sentimentu                 |
| **Statistická arbitráž / Pairs trading** | Obchodování návratu mezi korelovanými páry     | Korelace, cointegrace, z-score spreadu                  | Akcie, ETF, futures   | Intradenní – denní | 55–70 % | 1 : 1 až 1 : 2 | Nezávislé na trhu, stabilní výnos               | Nízké zisky, složitější implementace       |
| **Market Making / HFT**                  | Poskytování likvidity, zisk na spreadu         | Order book modely, volatility forecast                  | Krypto, futures, FX   | Sekundy – minuty   | 70–85 % | 0.1–0.5 : 1    | Vysoká frekvence zisků                          | Vyžaduje nízkou latenci, komplexní infra   |
| **Event-driven (fundamentální)**         | Reakce na zprávy, earnings, makro události     | NLP zpravodajství, kalendář událostí, sentiment analýza | Akcie, forex          | Hodiny – dny       | 40–60 % | 2–4 : 1        | Může mít velké zisky v krátkém čase             | Riziko gapů, nutnost rychlých dat          |
| **Portfolio / kvantitativní alokace**    | Diverzifikace strategií, minimalizace korelace | Markowitz, Black-Litterman, risk parity                 | ETF, indexy           | Týdny – měsíce     | 55–65 % | 1.5–3 : 1      | Nízká volatilita, stabilní růst                 | Složitější řízení korelace strategií       |


### Význam sloupců (metrik):

[Metriky strategií](Metriky%20strategi%C3%AD.md)

* **Winrate** = procento ziskových obchodů
* **Risk/Reward** = poměr průměrného zisku k průměrné ztrátě
* Vysoce výkonné systémy mívají **nízký winrate, ale vysoký R:R** (typicky trendové)
* Naopak systémy s **vysokým winrate** často vydělávají pomalu, ale jsou zranitelné při extrémních pohybech (mean reversion)


| Termín          | Význam                                   | Typická hodnota | Důležité poznámky                  |
| --------------- | ---------------------------------------- | --------------- | ---------------------------------- |
| **Winrate**     | % úspěšných obchodů                      | 30–70 %         | Neříká nic o velikosti zisků/ztrát |
| **Risk/Reward** | Poměr průměrného zisku k průměrné ztrátě | 1:1 až 3:1      | Vyšší R:R = menší tlak na přesnost |
