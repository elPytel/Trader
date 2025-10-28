# 📘 **SMA – Simple Moving Average**
- [📘 **SMA – Simple Moving Average**](#-sma--simple-moving-average)
    - [🧠 **Definice:**](#-definice)
    - [⚙️ **Matematický vzorec:**](#️-matematický-vzorec)
    - [📊 **Příklad:**](#-příklad)
    - [📈 **V praxi:**](#-v-praxi)
    - [⚖️ **Rozdíl oproti EMA**](#️-rozdíl-oproti-ema)
    - [🧮 **Výpočet v Pythonu (pandas):**](#-výpočet-v-pythonu-pandas)
    - [📋 **Shrnutí:**](#-shrnutí)
    - [💡 **Praktické kombinace:**](#-praktické-kombinace)

### 🧠 **Definice:**

> **SMA (jednoduchý klouzavý průměr)** je průměr cen za posledních *N* období, který se **posouvá s každou novou svíčkou**.
> Používá se k vyhlazení cenových dat, aby bylo snazší rozpoznat **trend** nebo **směr trhu**.


### ⚙️ **Matematický vzorec:**

$$
SMA_t = \frac{P_t + P_{t-1} + P_{t-2} + \dots + P_{t-(N-1)}}{N}
$$

kde:

* $SMA_t$ = hodnota SMA pro aktuální období
* $P_t$ = cena v aktuálním období (obvykle *Close*)
* $N$ = počet období (např. 10, 20, 50, 200)

### 📊 **Příklad:**

Pokud počítáš **SMA(5)** z denních uzavíracích cen:

```
Ceny: 100, 102, 104, 103, 105
SMA(5) = (100 + 102 + 104 + 103 + 105) / 5 = 102.8
```

Když přibude nový den (např. cena 106),
nejstarší hodnota (100) „vypadne“ a SMA se znovu přepočítá z posledních pěti.


### 📈 **V praxi:**

* **Rostoucí SMA** → potvrzuje rostoucí trend
* **Klesající SMA** → potvrzuje klesající trend
* **Cena nad SMA** → trh je v uptrendu
* **Cena pod SMA** → trh je v downtrendu
* **Křížení SMA(50) a SMA(200)** → známé signály „Golden Cross“ / „Death Cross“


### ⚖️ **Rozdíl oproti EMA**

| Vlastnost       | SMA                                  | EMA                              |
| --------------- | ------------------------------------ | -------------------------------- |
| Váhy dat        | Všechna období mají **stejnou váhu** | Novější data mají **větší váhu** |
| Reakce na změnu | Pomalejší                            | Rychlejší                        |
| Vhodné pro      | Dlouhodobé trendy                    | Krátkodobé nebo dynamické trhy   |

💡 Proto se SMA často používá jako „hladká základna“ (např. SMA200 = dlouhodobý trend),
zatímco EMA jako rychlejší prvek (např. EMA20 = krátkodobý směr).


### 🧮 **Výpočet v Pythonu (pandas):**

```python
import pandas as pd

# Např. 20denní SMA z uzavíracích cen
df['SMA20'] = df['Close'].rolling(window=20).mean()
```

### 📋 **Shrnutí:**

| Parametr     | Popis                                                    |
| ------------ | -------------------------------------------------------- |
| Název        | Simple Moving Average                                    |
| Zkratka      | SMA                                                      |
| Typ          | Trendový indikátor                                       |
| Vstupní data | Cena (nejčastěji Close)                                  |
| Citlivost    | Nízká (pomalejší než EMA)                                |
| Použití      | Určování směru trendu, potvrzení trendu, křížení průměrů |

### 💡 **Praktické kombinace:**

| Použití       | Krátkodobý MA | Dlouhodobý MA | Význam                   |
| ------------- | ------------- | ------------- | ------------------------ |
| Golden Cross  | SMA50         | SMA200        | Signál růstu trendu      |
| Death Cross   | SMA50         | SMA200        | Signál obratu dolů       |
| Swing trading | SMA10         | SMA50         | Vyhlazení menších pohybů |

