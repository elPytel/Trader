# Python Flask aplikace

- [Python Flask aplikace](#python-flask-aplikace)
  - [Jak spustit aplikaci](#jak-spustit-aplikaci)
  - [Stránka](#stránka)
- [Obchodování](#obchodování)
  - [Slovníček pojmů](#slovníček-pojmů)
  - [Algoritmické obchodování v praxi](#algoritmické-obchodování-v-praxi)
    - [💻 Pine Script](#-pine-script)
    - [🧠 TradingView](#-tradingview)
  - [TradingView](#tradingview)
    - [Pine Scriptu](#pine-scriptu)
      - [Jak ho použít:](#jak-ho-použít)
    - [🏦 IBKR (Interactive Brokers)](#-ibkr-interactive-brokers)
  - [IBKR - Interactive Brokers](#ibkr---interactive-brokers)
    - [IBKR API](#ibkr-api)
      - [Příklad integrace v praxi](#příklad-integrace-v-praxi)
  - [Backtesting](#backtesting)
    - [Hotové softwary pro backtesting](#hotové-softwary-pro-backtesting)
    - [Knihovny pro backtesting v Pythonu](#knihovny-pro-backtesting-v-pythonu)
      - [Ukázka s Backtesting.py](#ukázka-s-backtestingpy)
    - [Profesionální frameworky](#profesionální-frameworky)


## Jak spustit aplikaci

1. Ujistěte se, že máte nainstalované všechny potřebné knihovny uvedené v `requirements.txt`.
2. Spusťte aplikaci pomocí příkazu:

   ```bash
   python app.py
   ```

## Stránka

Webová stránka bude dostupná na [http://127.0.0.1:5000/](http://127.0.0.1:5000/) ve vašem prohlížeči.

# Obchodování

Jak vytvořit trading bota?
Jak otestovat paper trading?
Jak udělat analýzu obchodu na hystorických datech (aka backtesting)?
Jak vytvořit nekorelované portfolio?

## Slovníček pojmů
- **Broker** - prostředník pro obchodování na burze.
  - **IBKR** - Interactive Brokers, a je to jedna z největších a nejrespektovanějších broker společností na světě.
- **Systematické obchodování** - obchodování na základě předem definovaných pravidel.
- **Algoritmické obchodování** - obchodování pomocí počítačových programů.
- **Paper trading** - simulované obchodování bez reálných peněz.
- **Backtesting** - testování obchodní strategie na historických datech.

## Algoritmické obchodování v praxi

```css
[ Pine Script ] → analýza, indikátory
        ↓
[ TradingView ] → vizualizace, testování, alerty
        ↓
[ IBKR ] → reálné obchodování (příkazy na burze)
```

| Nástroj                           | Co to je                            | K čemu se používá                                         | Příklad použití                                        |
| --------------------------------- | ----------------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| 🧠 **TradingView**                | Webová platforma                    | Vizualizace grafů, analýzy, skripty                       | Sleduješ BTC/USD graf a spouštíš Pine Script indikátor |
| 💼 **IBKR (Interactive Brokers)** | Broker (obchodník s cennými papíry) | Reálné obchodování s akciemi, futures, forexem atd.       | Zadáš příkaz: „kup 10x AAPL“                           |
| 💻 **Pine Script**                | Programovací jazyk (od TradingView) | Tvorba indikátorů, strategií a alertů přímo v TradingView | Napíšeš skript, který ukazuje kdy nakoupit/prodat      |

### 💻 Pine Script

Je to jazyk používaný výhradně v TradingView.

- něco jako „mini-jazyk pro trhy“,
- používá se pro tvorbu indikátorů, strategií a alertů,
- nelze ho použít mimo TradingView (např. v Pythonu nebo IBKR).

> [!note] 📌 Typické použití:
„Chci indikátor, který ukáže, když Williams %R překročí 80.“

✅ Výhody:
- jednoduchý syntax,
- běží přímo v prohlížeči,
- rychlý backtest.

### 🧠 TradingView

Je to webová platforma pro analýzu trhů:

- přístupná z prohlížeče (žádná instalace),
- obsahuje grafy, indikátory, alerty a backtesting,
- můžeš si tam psát vlastní skripty v jazyce Pine Script.

> [!note] 📌 Typické použití:
„Chci sledovat RSI a MACD na grafu Bitcoinu a upozornění, když RSI < 30.“


## TradingView

[API Reference](https://www.tradingview.com/charting-library-docs/latest/api/)

### Pine Scriptu

Pine Script je jazyk pro skriptování, který se používá v TradingView pro vytváření vlastních indikátorů a strategií.

[Script Library](https://www.tradingview.com/scripts/)

[YouTube: The Art of Trading](https://www.youtube.com/@TheArtOfTrading)

#### Jak ho použít:

1. V TradingView otevři Pine Editor (dole na obrazovce).
2. Klikni na “Open” → “Upload from computer” a vyber svůj .pine soubor.
(Nebo prostě zkopíruj celý kód a vlož ho ručně do editoru.)
3. Ulož (Ctrl + S) a klikni na “Add to chart”.

> [!note] 📌 Poznámka: 
> TradingView používá Pine Script pouze uvnitř své platformy – tedy i když máš soubor s příponou .pine, mimo TradingView (např. v Pythonu nebo v jiném IDE) ho nespustíš.
> Slouží čistě jako přenosný formát kódu mezi uživateli TradingView.


### 🏦 IBKR (Interactive Brokers)

IBKR je reálný broker:
- drží tvé peníze a pozice,
- provádí příkazy na burze,
- má přístup k reálným tržním datům,
- má vlastní desktop aplikaci (TWS) a API pro automatizaci (např. Python).

> [!note] 📌 Typické použití:
„Můj Python bot pomocí IBKR API nakupuje akcie AAPL, když 10denní SMA překročí 50denní SMA.“

✅ Přednosti:
- přímé propojení s burzami,
- reálné i simulované obchodování (paper trading),
- přístup k téměř všem trhům na světě.

## IBKR - Interactive Brokers

### IBKR API

IBKR má API (rozhraní), přes které můžeš:

- 📡 napojit Python kód nebo backtestovací framework (např. Zipline, QuantConnect, Backtrader),
- 🧮 posílat reálné příkazy na burzu (market, limit, stop...),
- 🔁 synchronizovat data a portfolio,
- 💾 stahovat historická i živá data pro backtesting.

#### Příklad integrace v praxi

Pokud bys měl hotovou strategii v Pythonu, můžeš ji přes IBKR API napojit takto:

```python
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Připojení k TWS nebo IB Gateway

contract = Stock('AAPL', 'SMART', 'USD')
ib.reqMktData(contract, '', False, False)
```


## Backtesting

### Hotové softwary pro backtesting
| software | cena |
|----------|------|
| [RealTest](https://mhptrading.com/) | $389 USD |

### Knihovny pro backtesting v Pythonu

| Knihovna   | Výhody    | Poznámka       |
| -------------------------- | ------------------------------------- | --------------------------------- |
| **Backtrader**             | robustní, komunita, vizualizace       | klasika, trochu těžkopádný kód    |
| **vectorbt / vectorbtpro** | superrychlý (NumPy, Numba), elegantní | ideální pro kvanty                |
| **bt (by pmorissette)**    | jednoduchý, funkcionální styl         | méně kontroly nad exekucí         |
| **zipline**                | dříve Quantopian                      | zastaralý, ale dobrý konceptuálně |
| **Backtesting.py**         | velmi přehledný, čistý kód            | ideální pro začátek               |

#### Ukázka s Backtesting.py

```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01")

class SmaCross(Strategy):
    n1 = 20
    n2 = 50

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(close.rolling, self.n1).mean()
        self.sma2 = self.I(close.rolling, self.n2).mean()

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

bt = Backtest(data, SmaCross, cash=10_000, commission=.002)
stats = bt.run()
bt.plot()
print(stats)
```

### Profesionální frameworky

Když už chceš testovat portfolio strategií, ticková data, nebo režimy exekuce.

Příklady:
- Zipline / Zipline-live – integrovatelné s IBKR
- QuantConnect (cloud-based, Python + C#) – má i reálné nasazení
- vectorbtpro – GPU-akcelerovaný, ideální pro optimalizace


