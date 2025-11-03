# Portfolio 

- [Portfolio](#portfolio)
  - [Position sizing](#position-sizing)
  - [Využití kapitálu](#využití-kapitálu)
  - [Korelace strategií](#korelace-strategií)
  - [Denní volatilita portfolia](#denní-volatilita-portfolia)
    - [Anualizovaná volatilita portfolia](#anualizovaná-volatilita-portfolia)
  - [Délka drawdownu (ve dnech)](#délka-drawdownu-ve-dnech)
  - [Benchmark](#benchmark)
  - [Obchodní strategie](#obchodní-strategie)

## Position sizing

- fixní (stejná velikost pozice pro každý obchod)
- procentuální (určitý % z kapitálu na obchod)
- reinvestování vrámci strategie
- reinvestování vrámci portfolia

## Využití kapitálu

> [!note]
Při obchodování s přesažením 100% využití kapitálu, je potřeba nastavit obchodní systém tak aby obchodoval na páku.

> [!tip]
Při přesažení určitého % využití kapitálu (např. 80 %) je vhodné přestat otevírat nové pozice a počkat na uzavření stávajících obchodů.

## Korelace strategií

[Korelace strategií](./Strategie/Korelace_strategií.md)

- korelované (podobné trhy, podobné indikátory)
- nekorelované (různé trhy, různé indikátory)

Pokud je korelace blíží k **1**, strategie jsou velmi podobné a využívají kapitál ve stejný čas a stejným způsobem. 

Pokud je korelace blíží k **-1**, strategie jsou opačné a mohou vyvažovat riziko v portfoliu. Využívají sice kapitál ve stejný čas, ale v opačném směru.

Pokud je korelace blíží k **0**, strategie jsou nezávislé a diverzifikují portfolio a lépe využívají kapitál v čase.

> [!tip]
> Důležitý údaj je také korelace jednotlivých strategií s celkovým portfoliem.

## Denní volatilita portfolia

Hledáme portfolio s maximální denní volatilitou do **2-3%**.

### Anualizovaná volatilita portfolia

Hledáme portfolio s volatilitou do **20% ročně**.

## Délka drawdownu (ve dnech)

Vylepšíme přidáním dalších nekorelovaných strategií do portfolia. Cílem je mít průměrnou délku drawdownu pod **100 dní**.

## Benchmark

Porovnání výkonnosti portfolia s benchmarkem (např. S&P 500, BTCUSD, Gold).

Pro informativní účely je dobré mít srovnání výkonnosti našeho portfolia s nějakým benchmarkem. Umožní nám ti lépe posoudit, jak si naše strategie vedou v porovnání s trhem jako celkem. A zda by jsme neudělali lépe, kdyby jsme prostě jen koupili a drželi daný benchmark.

## Obchodní strategie

[Obchodní strategie](./Strategie/Obchodní%20strategie.md)

- **Mean reversion** - strategie, která se snaží profitovat z návratu ceny k průměru.
- **Momentum** - strategie, která se snaží profitovat z pokračování trendu.
