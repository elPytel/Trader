# Shortování: Proč je to rizikovější než běžný nákup (long)

- [Shortování: Proč je to rizikovější než běžný nákup (long)](#shortování-proč-je-to-rizikovější-než-běžný-nákup-long)
  - [📘 **Co je shortování (short selling)**](#-co-je-shortování-short-selling)
    - [📊 **Příklad:**](#-příklad)
  - [⚠️ **Proč může být ztráta z shortu obrovská**](#️-proč-může-být-ztráta-z-shortu-obrovská)
    - [🔹 1. **Neomezený potenciál ztráty**](#-1-neomezený-potenciál-ztráty)
    - [📊 **Příklad – když se cena obrátí proti tobě:**](#-příklad--když-se-cena-obrátí-proti-tobě)
    - [🔹 2. **Margin a nucené uzavření (margin call)**](#-2-margin-a-nucené-uzavření-margin-call)
    - [🔹 3. **Dividendové a poplatkové náklady**](#-3-dividendové-a-poplatkové-náklady)
    - [🔹 4. **Short squeeze (noční můra shortaře)**](#-4-short-squeeze-noční-můra-shortaře)
  - [🧠 **Shrnutí hlavních rizik shortování**](#-shrnutí-hlavních-rizik-shortování)
  - [💡 **Alternativy k čistému shortování**](#-alternativy-k-čistému-shortování)
  - [📋 **Závěr**](#-závěr)

## 📘 **Co je shortování (short selling)**

> **Shortování** znamená, že **vsadíš na pokles ceny** aktiva (např. akcie, krypta, ETF).

Technicky řečeno:

* „**půjčíš si**“ akcie (např. od brokera),
* **prodáš** je na trhu za současnou cenu,
* a **doufáš**, že později je **koupíš zpět levněji**,
  abys je **vrátil** a **vydělal rozdíl**.


### 📊 **Příklad:**

| Krok | Co uděláš                     | Cena akcie | Výsledek                  |
| ---- | ----------------------------- | ---------- | ------------------------- |
| 1️⃣  | Půjčíš si 1 akcii a prodáš ji | 100 $      | +100 $ hotovost           |
| 2️⃣  | Cena klesne na 60 $           |            |                           |
| 3️⃣  | Koupíš akcii zpět a vrátíš ji | 60 $       | Zisk = 100 – 60 = +40 $ ✅ |

➡️ Vydělal jsi 40 $.

Ale teď si ukážeme, proč je **short rizikovější než long**.


## ⚠️ **Proč může být ztráta z shortu obrovská**

### 🔹 1. **Neomezený potenciál ztráty**

Když kupuješ (long pozice):

* maximálně můžeš **ztratit 100 %**, protože cena nemůže klesnout pod nulu.

Když shortuješ:

* cena může růst **neomezeně vysoko** ⬆️,
  takže **tvoje ztráty mohou být teoreticky nekonečné**.


### 📊 **Příklad – když se cena obrátí proti tobě:**

| Krok | Cena akcie          | Co se stane                   | Výsledek                   |
| ---- | ------------------- | ----------------------------- | -------------------------- |
| 1️⃣  | Shortuješ za 100 $  | prodáš akcii, +100 $ hotovost |                            |
| 2️⃣  | Cena roste na 150 $ | musíš koupit zpět za 150 $    | Ztráta = –50 $             |
| 3️⃣  | Cena roste na 400 $ | panika, nucený výkup          | Ztráta = –300 $            |
| 4️⃣  | Teoreticky → ∞      | cena může dál růst            | Ztráty rostou bez limitu ❌ |

💥 Proto se říká:

> „Když shortuješ, **spíš na sopce**.“


### 🔹 2. **Margin a nucené uzavření (margin call)**

Shortování probíhá na **páku (margin)**.
Broker ti **půjčuje akcie** a vyžaduje, aby sis držel **zálohu (collateral)**.

* Když cena roste, ztrácíš peníze a **tvůj margin se snižuje**.
* Pokud poklesne pod určitou úroveň → broker tě **donutí zavřít pozici** se ztrátou.

To se jmenuje **margin call**.

👉 Broker tě tedy může „vynutit“ do ztráty ještě dřív, než by se trh otočil zpět.


### 🔹 3. **Dividendové a poplatkové náklady**

* Když jsi short akcie, musíš **vyplatit dividendy** držiteli akcie (protože jsi ji „půjčil“).
* Navíc platíš **úroky za vypůjčené akcie** (stock borrow fee).
* Tyto náklady se sčítají a snižují tvůj zisk.


### 🔹 4. **Short squeeze (noční můra shortaře)**

> **Short squeeze** = situace, kdy hodně obchodníků shortuje a cena náhle prudce stoupne.

Když cena začne růst:

1. Shortaři začnou **zavírat pozice** (kupují zpět → poptávka),
2. Tím **ještě víc zvyšují cenu**,
3. Což donutí další shortaře uzavírat,
4. A cena letí **exponenciálně nahoru** 🚀.

Známé příklady:

* **GameStop (2021)**
* **AMC, Tesla**

Zde lidé na shortech ztratili **miliardy**.


## 🧠 **Shrnutí hlavních rizik shortování**

| Riziko                   | Popis                                   | Jak se bránit                                          |
| ------------------------ | --------------------------------------- | ------------------------------------------------------ |
| **Neomezená ztráta**     | Cena může růst donekonečna              | Používej **stop-loss** nebo **opce** (protective call) |
| **Margin call**          | Broker uzavře pozici při poklesu účtu   | Neobchoduj s příliš velkou pákou                       |
| **Poplatky a dividendy** | Platíš úroky za vypůjčené akcie         | Sleduj borrow rate a dividendové termíny               |
| **Short squeeze**        | Masivní růst ceny kvůli nuceným nákupům | Nevstupuj do extrémně „shortovaných“ titulů            |


## 💡 **Alternativy k čistému shortování**

1. **Put opce (nákup PUT)**
   → Riziko omezené na zaplacené prémium, potenciál zisku při poklesu.

2. **Inverse ETF**
   → Např. `SDS`, `SH`, `PSQ` – rostou, když index klesá.

3. **Pair trading**
   → Short slabý titul a long silný (vyrovnáš tržní riziko).

4. **Risk management**
   → Nikdy nenech short běžet bez stop-lossu.

## 📋 **Závěr**

| Aspekt              | Long pozice             | Short pozice            |
| ------------------- | ----------------------- | ----------------------- |
| Maximální ztráta    | 100 %                   | Neomezená 💥            |
| Maximální zisk      | Neomezený               | 100 %                   |
| Směr sázky          | Růst ceny               | Pokles ceny             |
| Riziko margin callu | Nízké                   | Vysoké                  |
| Doporučeno pro      | Začátečníky i pokročilé | Pouze pokročilé tradery |


