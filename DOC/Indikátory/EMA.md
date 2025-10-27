# 📘 **EMA – Exponential Moving Average**

- [📘 **EMA – Exponential Moving Average**](#-ema--exponential-moving-average)
  - [🧠 **Definice:**](#-definice)
  - [⚙️ **Matematický vzorec:**](#️-matematický-vzorec)
  - [📊 **Příklad:**](#-příklad)
  - [📈 **V praxi:**](#-v-praxi)
  - [💡 **Proč se používá:**](#-proč-se-používá)
  - [📚 **Příklad použití v Pythonu (pandas):**](#-příklad-použití-v-pythonu-pandas)
  - [📋 **Shrnutí:**](#-shrnutí)


## 🧠 **Definice:**

> [!tip]
> **EMA (Exponenciální klouzavý průměr)** je typ klouzavého průměru, který **přikládá větší váhu novějším cenám**, a tím **rychleji reaguje na změny ceny** než jednoduchý klouzavý průměr (SMA – Simple Moving Average).

Jinými slovy, EMA ti ukazuje „vyhlazenou“ cenu, která se **přibližuje aktuálnímu trendu**, ale zároveň **ignoruje krátkodobý šum**.

## ⚙️ **Matematický vzorec:**

$$
EMA_t = \text{Cena}_t \times K + EMA_{t-1} \times (1 - K)
$$

kde:
$$
K = \frac{2}{N + 1}
$$

* $EMA_t$ = hodnota EMA pro aktuální období
* $Cena_t$ = aktuální cena (obvykle „close“)
* $N$ = počet období (např. 10, 20, 50, 200)
* $K$ = tzv. **vyhlazovací koeficient**


## 📊 **Příklad:**

Pokud používáš EMA(10):

* bereš posledních 10 svíček,
* nejnovější svíčky mají větší váhu než starší,
* EMA se proto „otáčí“ rychleji než SMA(10).


## 📈 **V praxi:**

* **Rostoucí EMA** → potvrzuje rostoucí trend
* **Klesající EMA** → potvrzuje klesající trend
* **Křížení EMA** (např. EMA(50) nad EMA(200)) → klasický trendový signál („Golden Cross“ / „Death Cross“)


## 💡 **Proč se používá:**

* Rychleji reaguje na nové informace než SMA
* Méně „zpožděná“
* Lépe funguje v trendových strategiích
* Snadno použitelná v algoritmech i manuálním tradingu


## 📚 **Příklad použití v Pythonu (pandas):**

```python
import pandas as pd

# Např. 20denní EMA z uzavíracích cen
df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
```


## 📋 **Shrnutí:**

| Vlastnost    | Popis                                               |
| ------------ | --------------------------------------------------- |
| Název        | Exponential Moving Average                          |
| Zkratka      | EMA                                                 |
| Typ          | Trendový indikátor                                  |
| Vstupní data | Cena (obvykle Close)                                |
| Citlivost    | Vyšší než SMA (rychlejší reakce)                    |
| Použití      | Identifikace trendu, křížení průměrů, trailing stop |

