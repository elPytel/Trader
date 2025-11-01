# Dopad změny timeframe na indikátor

- [Dopad změny timeframe na indikátor](#dopad-změny-timeframe-na-indikátor)
  - [🎛️ Analogie: indikátory = **digitální filtry**](#️-analogie-indikátory--digitální-filtry)
  - [🔍 SMA jako **low-pass filtr**](#-sma-jako-low-pass-filtr)
    - [📊 Příklad:](#-příklad)
  - [📈 Dopad na ostatní indikátory](#-dopad-na-ostatní-indikátory)
  - [🧠 Problém aliasingu](#-problém-aliasingu)
  - [📏 Přepočet periody mezi timeframe](#-přepočet-periody-mezi-timeframe)
    - [Ukázka v jupyter notebooku](#ukázka-v-jupyter-notebooku)
  - [🧩 Shrnutí dopadů změny „vzorkovací frekvence“](#-shrnutí-dopadů-změny-vzorkovací-frekvence)
  - [💡Praktické doporučení](#praktické-doporučení)


## 🎛️ Analogie: indikátory = **digitální filtry**

V technické analýze pracuješ se **signálem (cenou)**, který je **vzorkován v čase** – každá svíčka je jeden vzorek.

* **Týdenní graf:** 1 svíčka = 1 týden
* **Denní graf:** 1 svíčka = 1 den
* **Hodinový graf:** 1 svíčka = 1 hodina

➡️ Čím jemnější timeframe, tím **vyšší vzorkovací frekvence**.
A stejně jako v DSP platí:

> Při změně vzorkovací frekvence se mění charakteristika filtrů (indikátorů).


| DSP svět             | Trading svět       |
| -------------------- | ------------------ |
| Signál               | Cena               |
| Vzorkovací frekvence | Timeframe          |
| Filtr (low-pass)     | SMA / EMA          |
| Frekvenční spektrum  | Volatilita / noise |
| Aliasing             | Falešné signály    |
| Normalizace vzorků   | Přepočet periody   |

## 🔍 SMA jako **low-pass filtr**

Simple Moving Average (SMA) je v podstatě **lineární dolní propust (low-pass filter)**:

* Propouští pomalé (nízkofrekvenční) změny – tj. **dlouhodobý trend**,
* Tlumi rychlé (vysokofrekvenční) změny – tj. **šum**.

Při přechodu z týdenního grafu na hodinový:

* stejná **délka periody (např. SMA(20))** znamená **jinou fyzikální délku času**,
* a tím i jinou „propustnost“ filtru.


### 📊 Příklad:

| Graf     | SMA(20) pokrývá      | Relativní vyhlazení   |
| -------- | -------------------- | --------------------- |
| Týdenní  | 20 týdnů = ~5 měsíců | velmi pomalý filtr    |
| Denní    | 20 dní = ~1 měsíc    | střední filtr         |
| Hodinový | 20 hodin = <1 den    | extrémně rychlý filtr |

Na hodinovém grafu tak SMA(20) zachytí drobné mikrotrendy, ale nebude odrážet „velký trend“, který jsi viděl na týdenním grafu.


## 📈 Dopad na ostatní indikátory

Stejný princip platí pro **EMA, RSI, MACD, Bollinger Bands** atd.
Každý z nich je matematicky odvozený z časové řady cen → tedy také **frekvenčně závislý**.

| Indikátor       | Ekvivalentní filtr / reakce na frekvenci                             |
| --------------- | -------------------------------------------------------------------- |
| SMA             | lineární low-pass                                                    |
| EMA             | exponenciální low-pass (rychlejší odezva)                            |
| MACD            | rozdíl dvou low-pass filtrů → pásmová propust                        |
| RSI / Stoch     | měří relativní rychlost – reaguje na vysoké frekvence                |
| Bollinger Bands | závisí na směrodatné odchylce → tedy na rozptylu (amplitudě signálu) |

Když tedy **zvýšíš sampling rate (přejdeš na nižší timeframe)**,
vstupní signál má **více šumu (vysokofrekvenčních složek)** → indikátory reagují nervózněji, často „překmitávají“.


## 🧠 Problém aliasingu

Tady vstupuje **aliasing** – typický problém při zpracování signálů.
Když přecházíš z vyššího timeframe na nižší bez úpravy parametrů:

* Bereš *více vzorků* z téhož pohybu → indikátor vidí „šum“, který na vyšším timeframe neexistoval.
* Pokud neměníš „okno“ (např. SMA(20)), mění se *frekvenční charakteristika* filtru.

Výsledek:

* **Na nižším timeframe** dostaneš více falešných signálů.
* **Na vyšším timeframe** indikátor reaguje později, ale stabilněji.


## 📏 Přepočet periody mezi timeframe

Chceš-li zachovat **ekvivalentní časový horizont**, musíš přepočítat periodu podle poměru timeframe:

$$
N_{nové} = N_{původní} \times \frac{T_{původní}}{T_{nové}}
$$

Např. přechod z týdenního grafu (1 svíčka = 5 dní) na hodinový (1 svíčka = 1 hodina):

$$
N_{nové} = 20 \times \frac{5 \times 24}{1} = 2400
$$

➡️ SMA(20) na týdenním grafu odpovídá zhruba SMA(2400) na hodinovém grafu.
(Tedy 2400 hodin ≈ 20 týdnů × 5 dní × 24 hodin.)

### Ukázka v jupyter notebooku

[Ukázkový notebook](./Dopad%20změny%20timeframe%20na%20indikátor.ipynb)


## 🧩 Shrnutí dopadů změny „vzorkovací frekvence“

| Změna timeframe                          | Dopad na indikátory               | Dopad na signály                                |
| ---------------------------------------- | --------------------------------- | ----------------------------------------------- |
| Přechod z týdenního na hodinový          | Více dat → vyšší šum              | Více falešných signálů, vyšší frekvence obchodů |
| Přechod z hodinového na týdenní          | Méně dat → méně šumu              | Méně signálů, ale stabilnější                   |
| Zachování stejné periody (např. SMA(20)) | Mění se délka okna v reálném čase | Mění se „rychlost“ filtru                       |
| Úprava periody podle timeframe           | Zachová se stejné měřítko trendu  | Konzistentní s původním signálem                |


## 💡Praktické doporučení

1. **Nemyň timeframe bez přepočtu parametrů** – vždy si ověř, že „20“ na hodinovém grafu znamená totéž co „20“ na denním jen v čase, ne v jednotkách.
2. **Testuj na datech s různou granularitou** – strategie, která funguje na denních datech, často selže na minutových, pokud nejsou přepočteny filtry.
3. **Používej multi-timeframe analýzu** – kombinuj pomalý filtr (např. EMA200 z denních dat) s rychlým z nižšího timeframe.
4. **Mysli v časových jednotkách, ne v počtech svíček.**


