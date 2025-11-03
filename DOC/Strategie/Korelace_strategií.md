# Korelace strategií a efektivní využití kapitálu

- [Korelace strategií a efektivní využití kapitálu](#korelace-strategií-a-efektivní-využití-kapitálu)
  - [🧩 Co je „korelace strategií“ v kontextu portfolia](#-co-je-korelace-strategií-v-kontextu-portfolia)
  - [⚖️ Proč na korelaci záleží při využití kapitálu](#️-proč-na-korelaci-záleží-při-využití-kapitálu)
    - [🧮 Ilustrace (zjednodušený příklad)](#-ilustrace-zjednodušený-příklad)
  - [💡 Prakticky: vliv korelace na využití kapitálu](#-prakticky-vliv-korelace-na-využití-kapitálu)
  - [🔬 Jak to modelovat kvantitativně](#-jak-to-modelovat-kvantitativně)
  - [🧠 Shrnutí dopadu korelace na využití kapitálu](#-shrnutí-dopadu-korelace-na-využití-kapitálu)
  - [🧩 Doporučení pro portfolio systematických strategií](#-doporučení-pro-portfolio-systematických-strategií)
  - [📈 Bonus – vizualizace](#-bonus--vizualizace)


## 🧩 Co je „korelace strategií“ v kontextu portfolia

V tradingu korelace znamená, **jak podobně se pohybují výnosy dvou strategií** v čase.

* Korelace **+1** → strategie dělají *vždy totéž* (zisky a ztráty současně)
* Korelace **0** → strategie jsou *nezávislé* (náhodné vztahy)
* Korelace **–1** → strategie dělají *opačné pohyby* (zisk jedné = ztráta druhé)

Matematicky:
$$
\rho_{A,B} = \frac{\text{cov}(r_A, r_B)}{\sigma_A \cdot \sigma_B}
$$
kde:
- $r_A, r_B$ jsou výnosy jednotlivých strategií.

> [!info]
> Zjednodušeně můžeme na korelaci nahlížet jako součet absolutních hodnot rozdílů mezi dvěma signály v čase, normalizovaný jejich volatilitou.


## ⚖️ Proč na korelaci záleží při využití kapitálu

Když kombinuješ více strategií, **nepoužíváš kapitál lineárně**.
Celková alokace sice může být 100 %, ale *efektivní riziko* (a tedy i „využití kapitálu“) se mění podle vzájemné korelace.


### 🧮 Ilustrace (zjednodušený příklad)

Čistě školní příklad na ukázku: [Korelace mezi funkcemi sinus](./Correlation_Basics_Sinusoids.ipynb)


| Strategie                            | Kapitál | Volatilita | Korelace | Oček. výnos |
| ------------------------------------ | ------- | ---------- | -------- | ----------- |
| A                                    | 50 %    | 10 %       | –        | 8 %         |
| B                                    | 50 %    | 10 %       | **+1.0** | 8 %         |
| **Portfolio (A+B)**                  | 100 %   | 10 %       | –        | 8 %         |
| **Portfolio (nekorelované)**         | 100 %   | **7.1 %**  | **0.0**  | 8 %         |
| **Portfolio (negativně korelované)** | 100 %   | **5 %**    | **–0.5** | 8 %         |

🧠 Výsledek:

* Při **korelovaných strategiích** (ρ≈1) – volatilita a drawdown se *nesníží*, efektivní využití kapitálu zůstává stejné.
* Při **nekorelovaných strategiích** – kolísání se *zmenší*, takže můžeš **zvýšit pozice** (lepší využití kapitálu při stejném riziku).
* Při **opačně korelovaných** – můžeš držet **větší celkový objem pozic** a přitom mít stabilnější equity (nižší drawdown).


## 💡 Prakticky: vliv korelace na využití kapitálu

Představ si, že máš 2 strategie, každá s rizikem 2 % kapitálu na obchod.

| Korelace | Efektivní riziko portfolia | Poznámka                            |
| -------- | -------------------------- | ----------------------------------- |
| +1       | 4 %                        | Riziko se sčítá                     |
| 0        | √(2² + 2²) / √2 ≈ 2.8 %    | Částečná nezávislost                |
| –1       | 0 %                        | Rizika se vyruší (ideální vyvážení) |

➡️ Pokud jsou strategie **nekorelované**, můžeš použít *více strategií současně* při *stejném celkovém riziku*,
čili **efektivněji využíváš kapitál**.


## 🔬 Jak to modelovat kvantitativně

Celková volatilita portfolia $\sigma_p$ ze strategií $1…n$:

$$
\sigma_p = \sqrt{w^T \Sigma w}
$$

kde:

* $w$ = vektor vah jednotlivých strategií (např. 0.5, 0.5),
* $\Sigma$ = **kovarianční matice výnosů**.

V Pythonu (NumPy/Pandas) to vypadá takto:

```python
import numpy as np
import pandas as pd

# simulované denní výnosy dvou strategií
np.random.seed(42)
r1 = np.random.normal(0.001, 0.02, 250)
r2 = np.random.normal(0.001, 0.02, 250)
r2 = 0.5 * r1 + 0.5 * np.random.normal(0, 0.02, 250)  # částečně korelované

returns = pd.DataFrame({"A": r1, "B": r2})

# Kovarianční matice a volatilita portfolia
weights = np.array([0.5, 0.5])
cov_matrix = returns.cov()
portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)
corr = returns.corr()

print("Korelace strategií:\n", corr)
print("Volatilita portfolia:", round(portfolio_vol, 4))
```

Můžeš si s tím hrát — změnit `r2 = 1.0 * r1` (plná korelace) nebo `r2 = -1.0 * r1` (opačná) a sledovat, jak se mění celková volatilita.


## 🧠 Shrnutí dopadu korelace na využití kapitálu

| Typ vztahu          | Korelace (ρ)   | Dopad na portfolio                          | Dopad na využití kapitálu              |
| ------------------- | -------------- | ------------------------------------------- | -------------------------------------- |
| Vysoce korelované   | +0.8 až +1.0   | Výnosy i ztráty spolu → riziko se nesnižuje | Kapitál využit „dvakrát na totéž“      |
| Nekorelované        | 0.0 ± 0.2      | Diverzifikace, nižší drawdown               | Lepší efektivní využití                |
| Negativní korelace  | –0.3 až –1.0   | Vyvažují se ztráty                          | Umožňuje vyšší alokaci, menší kolísání |
| Nestabilní korelace | mění se v čase | Nevyzpytatelné portfolio chování            | Nutné sledovat adaptivně               |


## 🧩 Doporučení pro portfolio systematických strategií

1. **Měř korelace výnosů**, ne výsledků obchodů – denní/ týdenní P&L dává reálnější obrázek.
2. **Sleduj dynamiku korelace v čase** (rolling correlation). Korelace se může v různých fázích trhu měnit.
3. **Kombinuj trhy i logiky** (trend + mean reversion, akcie + krypto + futures).
4. **Optimalizuj váhy podle rizika**, ne podle zisku (risk parity, volatility targeting).
5. **Omez cross-margin efekt** – strategie, které ztrácí zároveň, by neměly sdílet kapitál.


## 📈 Bonus – vizualizace

V portfoliu si můžeš zobrazit korelace strategií jako heatmapu:

```python
import seaborn as sns
sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", center=0)
```

Tak hned vidíš, které strategie se překrývají a které přidávají diverzifikaci.


