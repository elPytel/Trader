# Hedging: Zajištění proti riziku cenových pohybů

- [Hedging: Zajištění proti riziku cenových pohybů](#hedging-zajištění-proti-riziku-cenových-pohybů)
  - [🧩 Definice: Co je hedging](#-definice-co-je-hedging)
    - [⚖️ Princip](#️-princip)
  - [🌾 Příklad z komodit (klasický hedging)](#-příklad-z-komodit-klasický-hedging)
    - [✅ Řešení:](#-řešení)
  - [💼 Příklad z investování](#-příklad-z-investování)
  - [📊 Hedging v portfoliu strategií](#-hedging-v-portfoliu-strategií)
    - [Například:](#například)
  - [🔢 Kvantitativní pohled](#-kvantitativní-pohled)
  - [🧠 Shrnutí](#-shrnutí)


## 🧩 Definice: Co je hedging

> **Hedging** = strategie, která **snižuje nebo eliminuje riziko nepříznivého pohybu ceny** aktiva.

Jinými slovy:
📉 chráníš se před poklesem (nebo růstem, pokud jsi short), tím, že **otevřeš opačnou pozici** nebo **použiješ nástroj, který ti kompenzuje ztrátu**.

[🎥youtube: Hedging Explained - The Insurance of Investing](https://www.youtube.com/watch?v=AEuCl2FmJ-Y)

### ⚖️ Princip

Máš **hlavní pozici**, která je citlivá na tržní riziko (např. držíš akcie, nebo máš zásobu pšenice).
Otevřeš **zajišťovací pozici (hedge)**, která vydělává, když ta hlavní ztrácí.

➡️ Zisk z hedge **kompenzuje** ztrátu z hlavní pozice.


## 🌾 Příklad z komodit (klasický hedging)

Řekněme, že jsi **farmář**, který bude za 3 měsíce sklízet **pšenici**.

* Dnes je cena pšenice **240 USD/t**.
* Bojíš se, že za 3 měsíce **cena klesne** → tvůj příjem bude nižší.

### ✅ Řešení:

Prodáš **futures kontrakt na pšenici (ZW=F)** dnes.
To je tvůj **hedge**.

* Pokud cena za 3 měsíce klesne, ztrácíš na reálné pšenici,
  ale **vyděláš na futures** (short futures zisky).
* Pokud cena stoupne, ztratíš na futures,
  ale **získáš na prodeji sklizně**.

💰 Celkově je tvůj výnos **stabilnější** → eliminoval jsi cenové riziko.


## 💼 Příklad z investování

Máš portfolio akcií v hodnotě 100 000 USD a bojíš se krátkodobého poklesu trhu.

Můžeš:

* koupit **put opci** na index S&P 500 (např. SPY) → vydělá při poklesu,
* nebo shortnout **futures na index**.

➡️ Ztráty na akciích vykompenzuje zisk z hedgingu.


## 📊 Hedging v portfoliu strategií

V kontextu strategie, korelace, využití kapitálu:

> Hedging znamená **kombinovat strategie nebo instrumenty tak, aby celkové portfolio bylo méně citlivé na tržní riziko**.

### Například:

| Strategie       | Směr              | Trh        | Účel                 |
| --------------- | ----------------- | ---------- | -------------------- |
| Trend-following | long při růstu    | akcie      | vydělává v růstu     |
| Mean reversion  | short při extrému | stejný trh | vydělává při korekci |
| Long volatility | opce (VIX)        | volatilita | chrání při krizích   |

👉 Tyto strategie se navzájem **hedgují**, protože **nejsou korelované** nebo mají **opačné fáze ziskovosti**.


## 🔢 Kvantitativní pohled

Hedging může být:

* **1:1** – úplné zajištění (např. 1 kontrakt futures = 1 jednotka aktiva)
* **částečný (partial hedge)** – snižuje riziko jen částečně (např. 50 %)
* **dynamický (rebalancovaný)** – mění se podle volatility (např. delta hedging u opcí)

Matematicky můžeš spočítat optimální velikost hedge:
$$
h^* = \rho \frac{\sigma_S}{\sigma_F}
$$
kde:
- $h^*$ = hedge ratio,
- $\rho$ = korelace mezi aktivem a zajišťovacím instrumentem,
- $\sigma_S$, $\sigma_F$ = volatilita aktiva a futures.


## 🧠 Shrnutí

| Aspekt         | Popis                                         |
| -------------- | --------------------------------------------- |
| Cíl            | Snížit riziko nepříznivého pohybu ceny        |
| Jak            | Držením opačné pozice nebo derivátu           |
| Kde se používá | Komodity, měny, akcie, portfolia              |
| Typy           | Futures hedge, opční hedge, strategický hedge |
| Nevýhoda       | Snižuje i potenciální zisk (něco za něco)     |
| Výsledek       | Stabilnější výnos, menší drawdown             |

