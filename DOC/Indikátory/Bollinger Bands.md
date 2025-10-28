# Bollinger Bands (BB)

- [Bollinger Bands (BB)](#bollinger-bands-bb)
  - [📘 **Definice: Bollinger Bands (BB)**](#-definice-bollinger-bands-bb)
    - [⚙️ **Matematický základ**](#️-matematický-základ)
    - [📈 **Jak to vypadá**](#-jak-to-vypadá)
  - [💡 **Jak Bollinger Bands interpretovat**](#-jak-bollinger-bands-interpretovat)
    - [🧠 **Důležité principy**](#-důležité-principy)
    - [⚖️ **Parametry, které můžeš ladit**](#️-parametry-které-můžeš-ladit)
    - [🧮 **Výpočet v Pythonu:**](#-výpočet-v-pythonu)
    - [📊 **Příklad použití**](#-příklad-použití)
    - [📋 **Shrnutí**](#-shrnutí)

## 📘 **Definice: Bollinger Bands (BB)**

> **Bollinger Bands** jsou indikátor složený ze **tří linií**, který měří **volatilitu trhu** okolo klouzavého průměru.
>
> Pásma se **rozšiřují**, když je trh volatilní, a **zužují**, když se trh uklidňuje.


### ⚙️ **Matematický základ**

Indikátor tvoří tři křivky:

$$
\begin{aligned}
\text{Střední pásmo (Middle Band)} &= SMA(N) \\
\text{Horní pásmo (Upper Band)} &= SMA(N) + k \times \sigma \\
\text{Dolní pásmo (Lower Band)} &= SMA(N) - k \times \sigma
\end{aligned}
$$

kde:

* $SMA(N)$ = **jednoduchý klouzavý průměr** z posledních N období
* $\sigma$ = **směrodatná odchylka** ceny (měří volatilitu)
* $k$ = **koeficient** – obvykle 2

Standardní nastavení: **Bollinger Bands (20, 2)**
➡️ tedy SMA(20) a 2× směrodatná odchylka.


### 📈 **Jak to vypadá**

```
    Horní pásmo  → SMA(20) + 2σ
        ↑
        │
    Cena (kolísá uvnitř)
        │
        ↓
    Dolní pásmo  → SMA(20) - 2σ
```

Cenu obklopují dvě „pásma“ – jako obálka kolem ní.
Přibližně **95 % všech cen** by se mělo nacházet uvnitř těchto pásem, pokud se trh chová normálně.


## 💡 **Jak Bollinger Bands interpretovat**

| Situace                          | Co to znamená                    | Typická strategie                  |
| -------------------------------- | -------------------------------- | ---------------------------------- |
| **Cena se dotýká horního pásma** | Trh je „překoupený“              | Možný návrat dolů (mean reversion) |
| **Cena se dotýká dolního pásma** | Trh je „přeprodaný“              | Možný návrat nahoru                |
| **Pásma se rozšiřují**           | Roste volatilita                 | Trh se „rozhýbává“                 |
| **Pásma se zužují („squeeze“)** | Nízká volatilita, hrozí breakout | Příprava na silný pohyb            |


### 🧠 **Důležité principy**

1. **Dotyk pásma ≠ signál** → znamená pouze extrémní pozici, ne nutně obrat.
2. **Squeeze** (zúžení pásem) je často předzvěst velkého trendu nebo proražení.
3. Nejlépe fungují v **bočním trhu** (range-bound).
4. Lze kombinovat s jinými indikátory (např. RSI, MACD) pro potvrzení signálu.

### ⚖️ **Parametry, které můžeš ladit**

| Parametr  | Význam                      | Typická hodnota         |
| --------- | --------------------------- | ----------------------- |
| `N`       | Počet období pro SMA        | 20                      |
| `k`       | Násobek směrodatné odchylky | 2                       |
| Zdroj dat | obvykle **Close**           | můžeš zkusit i High/Low |

### 🧮 **Výpočet v Pythonu:**

```python
import pandas as pd

# Bollinger Bands (20, 2)
df['SMA20'] = df['Close'].rolling(window=20).mean()
df['STD20'] = df['Close'].rolling(window=20).std()

df['Upper'] = df['SMA20'] + 2 * df['STD20']
df['Lower'] = df['SMA20'] - 2 * df['STD20']
```


### 📊 **Příklad použití**

* **Mean reversion strategie:**

  * Když se cena dotkne *dolního pásma* → kupuj
  * Když se dotkne *horního pásma* → prodávej
  * Zavři pozici, když se cena vrátí ke střednímu pásmu (SMA)

* **Breakout strategie:**

  * Po dlouhém zúžení (squeeze) → vstup do směru proražení (nad horní / pod dolní pásmo)


### 📋 **Shrnutí**

| Vlastnost            | Popis                                   |
| -------------------- | --------------------------------------- |
| Název                | Bollinger Bands                         |
| Typ                  | Volatilita / Mean reversion indikátor   |
| Složení              | SMA + 2 pásma dle směrodatné odchylky   |
| Standardní nastavení | (20, 2)                                 |
| Použití              | Určení extrémů ceny, detekce volatility |
| Výhoda               | Přizpůsobuje se dynamicky trhu          |
| Nevýhoda             | V trendu často dává falešné signály     |
