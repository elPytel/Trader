# Metriky strategií

- [Metriky strategií](#metriky-strategií)
  - [Zhodnocení](#zhodnocení)
    - [📊 Příklad:](#-příklad)
  - [Drawdown](#drawdown)
    - [📊 Příklad:](#-příklad-1)
  - [🎯 Winrate (míra úspěšnosti obchodů)](#-winrate-míra-úspěšnosti-obchodů)
    - [📘 Definice:](#-definice)
    - [📊 Příklad:](#-příklad-2)
    - [🧠 Poznámka:](#-poznámka)
  - [⚖️ Risk/Reward Ratio (poměr rizika k výnosu)](#️-riskreward-ratio-poměr-rizika-k-výnosu)
    - [📘 Definice:](#-definice-1)
    - [📊 Příklad:](#-příklad-3)
  - [💡 Jak Winrate a R:R spolu souvisí](#-jak-winrate-a-rr-spolu-souvisí)
    - [📈 Příklad porovnání:](#-příklad-porovnání)
  - [📘 Definice: Sharpe Ratio](#-definice-sharpe-ratio)
    - [⚙️ Matematický vzorec:](#️-matematický-vzorec)
    - [📊 Příklad:](#-příklad-4)
    - [📈 Jak interpretovat hodnoty](#-jak-interpretovat-hodnoty)
    - [🧠 Intuitivně:](#-intuitivně)
    - [💡 Proč je důležité:](#-proč-je-důležité)
    - [📚 Příklad výpočtu v Pythonu:](#-příklad-výpočtu-v-pythonu)
    - [📋 Shrnutí](#-shrnutí)


## Zhodnocení

Zhodnocení (Return) je základní metrika, která udává procentuální změnu hodnoty investice za určité období.
Vypočítá se jako:

$$
\text{Zhodnocení} = \frac{\text{Konečná hodnota} - \text{Počáteční hodnota}}{\text{Počáteční hodnota}} \times 100%
$$

### 📊 Příklad:

Pokud jsi začal s 10 000 Kč a po roce máš 12 000 Kč:
$$
\text{Zhodnocení} = \frac{12 000 - 10 000}{10 000} \times 100\% = 20\%
$$

## Drawdown

Drawdown měří pokles hodnoty investice od jejího vrcholu k nejnižšímu bodu před dosažením nového vrcholu.
Vypočítá se jako:

$$
\text{Drawdown} = \frac{\text{Vrcholová hodnota} - \text{Dno}}{\text{Vrcholová hodnota}} \times 100\%
$$

### 📊 Příklad:

Pokud máš investici, která dosáhla vrcholu 15 000 Kč a poté klesla na 10 000 Kč, drawdown se vypočítá takto:

$$
\text{Drawdown} = \frac{15 000 - 10 000}{15 000} \times 100\% = 33.33\%
$$

## 🎯 Winrate (míra úspěšnosti obchodů)

### 📘 Definice:

> **Winrate** udává, kolik procent tvých obchodů skončilo se ziskem.

Vyjadřuje **pravděpodobnost, že tvůj obchod bude ziskový**.
Získáš ho vydělením počtu ziskových obchodů celkovým počtem obchodů:

$$
\text{Winrate} = \frac{\text{Počet ziskových obchodů}}{\text{Celkový počet obchodů}} \times 100%
$$

### 📊 Příklad:

Máš 100 obchodů, z toho 45 ziskových a 55 ztrátových.

$$
\text{Winrate} = \frac{45}{100} \times 100% = 45%
$$

Tedy **45 % obchodů** vydělalo.


### 🧠 Poznámka:

* Vysoký winrate ≠ zisková strategie.
* Můžeš mít **nízký winrate** (např. 35 %) a **stále vydělávat**, pokud jsou výherní obchody dost velké.
* Proto se vždy hodnotí *spolu s* poměrem **Risk/Reward** 👇


## ⚖️ Risk/Reward Ratio (poměr rizika k výnosu)

### 📘 Definice:

> **Risk/Reward (R:R)** měří, kolik průměrně vyděláš na jeden ztracený dolar (nebo korunu).

Ukazuje **poměr průměrného zisku** k **průměrné ztrátě**.

$$
\text{Risk/Reward Ratio} = \frac{\text{Průměrný zisk na obchod}}{\text{Průměrná ztráta na obchod}}
$$


### 📊 Příklad:

* Průměrná ztráta = 100 Kč
* Průměrný zisk = 250 Kč

$$
\text{R:R} = \frac{250}{100} = 2.5
$$

Tedy **na každý ztracený 1 Kč vyděláš průměrně 2.5 Kč**.
Poměr **2:1 nebo vyšší** se považuje za velmi zdravý.

## 💡 Jak Winrate a R:R spolu souvisí

I strategie s malým winrate může být zisková, pokud má vysoký R:R.
Ziskovost strategie lze zjednodušeně zapsat jako:

$$
\text{Očekávaná hodnota (EV)} = (\text{Winrate} \times \text{Průměrný zisk}) - ((1 - \text{Winrate}) \times \text{Průměrná ztráta})
$$

Pokud EV > 0 → strategie dlouhodobě vydělává 💰


### 📈 Příklad porovnání:

| Typ strategie    | Winrate | Risk/Reward | Výsledek        |
| ---------------- | ------- | ----------- | --------------- |
| Trend-following  | 40 %    | 3 : 1       | ✅ Zisková       |
| Mean reversion   | 70 %    | 1 : 1       | ✅ Mírně zisková |
| Špatná strategie | 60 %    | 0.5 : 1     | ❌ Ztrátová      |

## 📘 Definice: Sharpe Ratio

> **Sharpe ratio** měří, jaký *nadvýnos* (zisk nad bezrizikovou sazbou) přináší strategie **v poměru k jejímu riziku (volatilitě)**.

Jinými slovy:

> Kolik zisku jsi získal za každý jednotkový „risk“, který jsi podstoupil.

**Sharpe ratio** (česky *Sharpeho poměr*) je jeden z **nejdůležitějších ukazatelů výkonnosti investiční nebo obchodní strategie**.
Používají ho fondy, algoritmičtí tradeři i kvantitativní analýzy, protože spojuje **výnos a riziko do jednoho čísla**.

### ⚙️ Matematický vzorec:

$$
S = \frac{R_p - R_f}{\sigma_p}
$$

kde:

* $S$ = Sharpe ratio
* $R_p$ = průměrný výnos portfolia nebo strategie
* $R_f$ = bezriziková úroková míra (např. výnos státních dluhopisů)
* $\sigma_p$ = směrodatná odchylka výnosů (měří volatilitu / riziko)


### 📊 Příklad:

* Průměrný měsíční výnos strategie: **2 %**
* Bezriziková sazba: **0.5 %**
* Směrodatná odchylka výnosů: **1 %**

$$
S = \frac{2 - 0.5}{1} = 1.5
$$

👉 Sharpe ratio = **1.5**

To znamená, že strategie vydělává **1.5 jednotky výnosu na každou jednotku rizika**.


### 📈 Jak interpretovat hodnoty

| Sharpe Ratio | Kvalita strategie | Interpretace                              |
| ------------ | ----------------- | ----------------------------------------- |
| < 0          | ❌ Ztrátová       | Lepší by bylo držet hotovost              |
| 0 – 1        | ⚠️ Slabá          | Riziko neodpovídá výnosu                  |
| 1 – 2        | ✅ Dobrá          | Vyvážený poměr rizika a výnosu            |
| 2 – 3        | 💪 Výborná        | Efektivní strategie                       |
| > 3          | 🚀 Výjimečná      | Typické pro HFT nebo krátkodobé algoritmy |


### 🧠 Intuitivně:

* Sharpe ratio **roste**, když:
  * výnosy jsou stabilní (nízká volatilita),
  * zisk je konzistentní,
  * a drawdowny jsou malé.
* Když strategie má stejné zisky, ale větší výkyvy → Sharpe ratio **klesne**.


### 💡 Proč je důležité:

* Umožňuje **porovnat různé strategie** bez ohledu na velikost kapitálu.
* Pomáhá vybrat „nejefektivnější“ strategii, ne nutně tu s nejvyšším ziskem.
* Používá se i v optimalizaci portfolií (např. Markowitzova teorie portfolia).


### 📚 Příklad výpočtu v Pythonu:

```python
import pandas as pd
import numpy as np

# Simulace denních výnosů strategie
returns = pd.Series([0.002, 0.003, -0.001, 0.004, 0.001])

# Bezriziková sazba (např. 5 % ročně ≈ 0.05 / 252 za den)
risk_free_rate = 0.05 / 252

# Výpočet Sharpe ratio (annualizované)
excess_returns = returns - risk_free_rate
sharpe_ratio = np.sqrt(252) * excess_returns.mean() / excess_returns.std()

print("Sharpe ratio:", round(sharpe_ratio, 2))
```

📈 Tento kód ti ukáže, jak Sharpe ratio přepočítat na roční bázi.


### 📋 Shrnutí

| Parametr           | Význam                                   |
| ------------------ | ---------------------------------------- |
| Název              | Sharpe Ratio                             |
| Měří               | Efektivitu výnosu vůči riziku            |
| Jednotka           | Bezrozměrná (číslo)                      |
| Ideální hodnota    | > 1 (dobrá), > 2 (výborná)               |
| Riziko měřené přes | Volatilitu (směrodatná odchylka výnosů)  |
| Použití            | Porovnání strategií, hodnocení portfolií |
