# Metriky strategií

- [Metriky strategií](#metriky-strategií)
  - [Zhodnocení](#zhodnocení)
    - [📊 Příklad:](#-příklad)
  - [Drawdown](#drawdown)
    - [📊 Příklad:](#-příklad-1)
  - [🎯 **Winrate (míra úspěšnosti obchodů)**](#-winrate-míra-úspěšnosti-obchodů)
    - [📘 Definice:](#-definice)
    - [📊 Příklad:](#-příklad-2)
    - [🧠 Poznámka:](#-poznámka)
  - [⚖️ **Risk/Reward Ratio (poměr rizika k výnosu)**](#️-riskreward-ratio-poměr-rizika-k-výnosu)
    - [📘 Definice:](#-definice-1)
    - [📊 Příklad:](#-příklad-3)
  - [💡 **Jak Winrate a R:R spolu souvisí**](#-jak-winrate-a-rr-spolu-souvisí)
    - [📈 Příklad porovnání:](#-příklad-porovnání)


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

## 🎯 **Winrate (míra úspěšnosti obchodů)**

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


## ⚖️ **Risk/Reward Ratio (poměr rizika k výnosu)**

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

## 💡 **Jak Winrate a R:R spolu souvisí**

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

