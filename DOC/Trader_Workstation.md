# Trader Workstation
- [Trader Workstation](#trader-workstation)
  - [Basket Trader](#basket-trader)
    - [CSV import](#csv-import)
  - [Python TWS API](#python-tws-api)
    - [Instalace \& Konfigurace TWS pro API](#instalace--konfigurace-tws-pro-api)
    - [Instalace TWS API](#instalace-tws-api)
      - [Python – Specifické nastavení](#python--specifické-nastavení)
    - [Placing Orders](#placing-orders)

## Basket Trader

TWS BasketTrader je výkonný nástroj, který je užitečný, když uživatel chce odeslat více objednávek najednou a sledovat průběh těchto objednávek.

Chcete-li získat přístup k BasketTrader z TWS, klikněte na oblast Nové okno v levém horním rohu, posuňte se dolů do sekce **Ostatní nástroje**, zvýrazněte **„Více pokročilých nástrojů“** a vyberte **BasketTrader**. 

BasketTrader se zobrazí jako samostatné okno. Nastavení a rozvržení datových sloupců BasketTrader můžete nakonfigurovat kliknutím na ikonu klíče v pravém horním rohu obrazovky.

- [interactivebrokers: Basket Trader](https://www.interactivebrokers.com/campus/trading-lessons/tws-baskettrader-create-a-basket/)

### CSV import

Nástroj TWS BasketTrader umožňuje importovat soubor **CSV** Basket do nástroje, což vám umožní upravit, odeslat a spravovat košík objednávek.

Chcete-li nahrát soubor košíku:
1. V rámci BasketTrader klikněte na tlačítko **Procházet**
2. V seznamu souborů vyberte **soubor**, který chcete nahrát
3. Klikněte na **Otevřít** pro načtení souboru.

Pokud si nejste jisti formátováním souboru CSV, doporučuje se nejprve exportovat testovací soubor z BasketTrader:
1. Zadejte několik testovacích objednávek do BasketTrader
2. V nabídce Soubor klikněte na Uložit košík jako..
3. Dejte svému souboru název a klikněte na Uložit.
4. Nyní můžete tento soubor otevřít pomocí tabulkového procesoru, jako je Excel.

- [How do I upload a CSV Basket file to BasketTrader?](https://www.interactivebrokers.com/lib/cstools/faq/#/content/64159770)


## Python TWS API

[campus: Python TWS API](https://www.interactivebrokers.com/campus/trading-course/python-tws-api/)

- Trader Workstation - plné GUI,
- IB Gateway - lehčí aplikace bez GUI, určená pouze pro API připojení.

### Instalace & Konfigurace TWS pro API

> [!warning]
> Chcete-li přijímat živá nebo historická data z API, je nejprve nutné mít v TWS povolena oprávnění pro živá data. Pro většinu typů nástrojů to vyžaduje nejprve mít živý financovaný účet s aktivními předplatnými tržních dat.

Po úplném přihlášení do TWS a jeho úplném načtení poprvé je nutné povolit nastavení pro připojení API a několik dalších, která se někteří uživatelé rozhodnou nakonfigurovat jinak pro své aplikace. Nastavení API lze nakonfigurovat v globální konfiguraci. Pro Trader Workstation vyberte **ozubené kolo** v pravém horním rohu. 

> [!note]
> Uživatelé IB Gateway by měli vidět možnost „Konfigurovat“ a „Nastavení“ pro spuštění stejného okna.

Po otevření globální konfigurace přejdete na **API** a poté na **Settings** vlevo. Nastavení nutné k povolení připojení soketového klienta pro Python je první zaškrtávací políčko označené **Enable ActiveX and Socket Clients**. Další nastavení, která ovlivňují počáteční připojení, jsou:
- Nastavení **„Pouze pro čtení“** je ve výchozím nastavení povoleno a zablokuje všechny objednávky API. Musí být **zrušeno** zaškrtnutí, aby byly povoleny jakékoli objednávky z API.
- **„Socket Port“** – Ve výchozím nastavení TWS používá pro živé relace port soketu **7496** a pro papírové relace **7497**. To jsou však pouze výchozí hodnoty a lze je upravit podle potřeby – port soketu v TWS musí být nakonfigurován tak, aby odpovídal portu soketu použitým ve funkci connect() klienta API.

> [!note]
> Na druhou stranu IB Gateway používá:
> - pro živé relace **4001** a,
> - pro papírové relace **4002**. 

> [!tip]
> Příklad konfigurace portu soketu v TWS:
> - Pro živé relace: **7496**
> - Pro papírové relace: **7497**

Některá další nastavení, která jsou nezbytná pro řešení problémů se zákaznickou podporou, se týkají protokolování API. Chcete-li povolit protokolování zpráv API pro řešení konkrétních problémů s API, existují tři pozoruhodná nastavení:
- **„Vytvořit protokol zpráv API“** – Používá se k vytvoření souboru protokolu API, který zaznamená všechny zprávy API.
- **„Zahrnout tržní data do souboru protokolu API“** – zahrne všechna tržní data vrácená touto žádostí do protokolu.
- **„Úroveň protokolování“** je rozbalovací nabídka pro úpravu informací přítomných v protokolech. Pokud je toto nastaveno na nejvyšší úroveň nazvanou „Detail“, protokoly API zdokumentují veškerý provoz API do a z Trader Workstation.

Po povolení těchto nastavení mohou uživatelé kliknout na **Použít** a poté na **OK** dole, aby potvrdili a uložili tyto změny.

- [campus: What is the TWS API?](https://www.interactivebrokers.com/campus/trading-lessons/what-is-the-tws-api/)
- [campus: Installing & Configuring TWS for the API](https://www.interactivebrokers.com/campus/trading-lessons/installing-configuring-tws-for-the-api/)
- [campus: Accessing the TWS Python API Source Code](https://www.interactivebrokers.com/campus/trading-lessons/accessing-the-tws-python-api-source-code/)

### Instalace TWS API
TWS API ke stažení a návody najdete na našem webu IBKR Campus v sekci [dokumentace TWS API](https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#paper-trading-limitations). Podobně jako jsme stahovali Trader Workstation, nyní můžeme vybrat sekci „Download the TWS API“ a poté tlačítko „TWS API Download Page“. Kliknutím na toto tlačítko budete přesměrováni na stránku s licenční smlouvou TWS API Non-Commercial License Agreement. Po odsouhlasení licence si můžete stáhnout stabilní nebo nejnovější verzi pro svůj operační systém.

Pro použití TWS API v Pythonu si budete muset stáhnout jednu z podporovaných verzí – stabilní nebo nejnovější – dostupných na [této](https://interactivebrokers.github.io/) stránce. API je neustále aktualizováno, proto doporučujeme tuto stránku pravidelně kontrolovat kvůli novým verzím.

#### Python – Specifické nastavení
Poté, co si stáhnete TWS API nebo IBJts. Je potřeba přejít do složky s instalací pomocí příkazového řádku (Command Prompt) nebo terminálu (Terminal) na Windows či Unixu. Ve složce najdete adresáře `samples` a `source`. Pro Python tutoriál přejděte do složky `source`, poté do `pythonclient`. 

> [!note]
> V základní konfiguraci se TWS API nainstaluje do složky `C:\TWS API\`. 

Vaše aktuální pracovní složka by tedy měla být `{TWS API}\source\pythonclient\`. V této složce najdete soubor `setup.py`. Tento soubor je potřeba spustit, aby se do vašeho IDE nainstalovaly nejnovější aktualizace pro Python a všechny potřebné knihovny pro TWS API.

Pro spuštění tohoto souboru zadejte příkaz:

~~`python setup.py install`~~

>[!warning]
> Z bezpečnostních důvodů nelze v nových instalacích Pythonu tento příkaz spustit a nainstalovat balíčky globálně bez administrátorských oprávnění. 

Doporučuje se použít [virtuální prostředí](Virtuální_prostředí.md) (virtual environment) nebo přidat přepínač `--user` k příkazu pro instalaci pouze pro aktuálního uživatele. Instalace pro aktuálního uživatele:
```bash
python setup.py install --user
```

Tímto příkazem spustíte soubor `setup.py` s instalací potřebného obsahu. Po několika okamžicích by měla být instalace dokončena.

Pro ověření úspěšné instalace můžete zadat:

```bash
python -m pip show ibapi
```

Tímto příkazem zobrazíte aktuálně nainstalovanou verzi balíčku. Pokud instalace proběhla správně, měla by se verze shodovat s verzí na webu. Například já vidím verzi 10.29 v obou případech.

Jako validační krok před psaním vlastního kódu spusťte některý z testovacích programů, které jsou součástí instalace API. Přejděte do složky `C:\TWS API\samples\Python\Testbed`, kde najdete několik programů.

Spusťte například:

```bash
python Program.py --port 7497
```

Tímto spustíte soubor `Program.py`. Pokud nezadáte argument `--port`, program se pokusí připojit na port **7496** (výchozí). Pokud vše funguje správně, uvidíte požadavky na kontrakty pro několik instrumentů a různé testovací případy.

### Placing Orders

- [campus: Placing Orders using TWS Python API](https://www.interactivebrokers.com/campus/trading-lessons/python-placing-orders/)
- [youtube: Placing Orders using TWS Python API](https://www.youtube.com/watch?v=vTXJ7v8ktis)