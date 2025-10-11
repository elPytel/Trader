import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# 🧭 Nastavení parametrů
# ----------------------------------------------------------
Tydnu = 26          # Počet týdnů
nasobek = 5         # Denní násobek (pro SMA okna)

# ----------------------------------------------------------
# 📥 Načtení dat z Yahoo Finance
# ----------------------------------------------------------
symbols = {
    "SPX": "^GSPC",   # S&P 500
    "USD": "DX=F",    # Dolarový index
    "GOLD": "GC=F",   # Zlato
    "BOND": "ZN=F"    # 10Y Bond Futures (spolehlivější než ZB=F)
}

data = {}
for key, sym in symbols.items():
    print(f"Stahuji {sym} ...")
    df = yf.download(sym, start="2020-01-01", progress=False, auto_adjust=False)
    if df is not None and 'Close' in df.columns:
        data[key] = df[['Close']].rename(columns={'Close': key})
    else:
        print(f"⚠️  Data {sym} nelze načíst.")
        continue

# Sloučení všech dat podle datumu
df = pd.concat(data.values(), axis=1).dropna()
print("\n✅ Načtená data:\n", df.tail())

# ----------------------------------------------------------
# 🧮 Výpočet indikátoru (analog PineScriptu)
# ----------------------------------------------------------
def compute_williams_value(price, divisor, weeks, nasobek):
    ratio = price / divisor * 100
    PaI2 = ratio.rolling(2 * nasobek, min_periods=1).mean()
    PaI22 = ratio.rolling(22 * nasobek, min_periods=1).mean()
    PaI222 = PaI2 - PaI22
    PaIHigh = PaI222.rolling(weeks * nasobek, min_periods=1).max()
    PaILow = PaI222.rolling(weeks * nasobek, min_periods=1).min()
    PaI1 = (PaI222 - PaILow) / (PaIHigh - PaILow) * 100
    return PaI1.clip(lower=0, upper=100)

# ----------------------------------------------------------
# 📈 Výpočet všech tří křivek
# ----------------------------------------------------------
PaIG = compute_williams_value(df["SPX"], df["GOLD"], Tydnu, nasobek)
PaID = compute_williams_value(df["SPX"], df["USD"], Tydnu, nasobek)
PaIT = compute_williams_value(df["SPX"], df["BOND"], Tydnu, nasobek)

# Sjednocení indexů a odstranění NaN
PaIG, PaID = PaIG.align(PaID, join='inner')
PaIG, PaIT = PaIG.align(PaIT, join='inner')
valid_mask = PaIG.notna() & PaID.notna() & PaIT.notna()

df_valid = df.loc[valid_mask.index]
PaIG = PaIG[valid_mask]
PaID = PaID[valid_mask]
PaIT = PaIT[valid_mask]

# ----------------------------------------------------------
# 🖼️ Vykreslení výsledků
# ----------------------------------------------------------
plt.figure(figsize=(12, 6))
plt.plot(df_valid.index, PaIG, color='gold', linewidth=2, label='Zlato')
plt.plot(df_valid.index, PaID, color='blue', linewidth=1, label='Dolar')
plt.plot(df_valid.index, PaIT, color='red', linewidth=1, label='Bondy')

# Extrémní pásma
plt.axhline(20, color='gray', linestyle='--', linewidth=1)
plt.axhline(75, color='gray', linestyle='--', linewidth=1)
plt.fill_between(df_valid.index, 20, 75, color='silver', alpha=0.2)

plt.title("Williams Value - Relativní síla SPX vůči Zlatu, Dolaru a Bondům")
plt.xlabel("Datum")
plt.ylabel("Hodnota (0–100)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
