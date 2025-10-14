# Trader Workstation
- [Trader Workstation](#trader-workstation)
  - [Basket Trader](#basket-trader)
    - [CSV import](#csv-import)
  - [Python TWS API](#python-tws-api)
    - [Installing \& Configuring TWS for the API](#installing--configuring-tws-for-the-api)
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

### Installing & Configuring TWS for the API

> [!warning]
> Chcete-li přijímat živá nebo historická data z API, je nejprve nutné mít v TWS povolena oprávnění pro živá data. Pro většinu typů nástrojů to vyžaduje nejprve mít živý financovaný účet s aktivními předplatnými tržních dat.

Po úplném přihlášení do TWS a jeho úplném načtení poprvé je nutné povolit nastavení pro připojení API a několik dalších, která někteří uživatelé rozhodnou nakonfigurovat jinak pro své aplikace. Nastavení API lze nakonfigurovat v globální konfiguraci. Pro Trader Workstation vyberte **ozubené kolo** v pravém horním rohu. 

> [!note]
> Uživatelé IB Gateway by měli vidět možnost „Konfigurovat“ a „Nastavení“ pro spuštění stejného okna.

Po zadání globální konfigurace mohou uživatelé přejít na **API** a poté na **Nastavení** vlevo. Nastavení nutné k povolení připojení soketového klienta pro Python je první zaškrtávací políčko označené **„Povolit ActiveX a Socket Clients“**. Další nastavení, která ovlivňují počáteční připojení, jsou:
- Nastavení **„Pouze pro čtení“** je ve výchozím nastavení povoleno a zablokuje všechny objednávky API. Musí být **zrušeno** zaškrtnutí, aby byly povoleny jakékoli objednávky z API.
- **„Socket Port“** – Ve výchozím nastavení TWS používá pro živé relace port soketu **7496** a pro papírové relace **7497**. 

> [!note]
> Na druhou stranu IB Gateway používá pro živé relace **4001** a pro papírové relace **4002**. To jsou však pouze výchozí hodnoty a lze je upravit podle potřeby – port soketu v TWS musí být nakonfigurován tak, aby odpovídal portu soketu použitým ve funkci connect() klienta API.

> [!tip]
> Příklad konfigurace portu soketu v TWS:
> - Pro živé relace: **7496**
> - Pro papírové relace: **7497**

Některá další nastavení, která jsou nezbytná pro eskalaci problémů s zákaznickou podporou, se týkají protokolování API. Chcete-li povolit protokolování zpráv API pro řešení konkrétních problémů s API, existují tři pozoruhodná nastavení:
- **„Vytvořit protokol zpráv API“** – Používá se k vytvoření souboru protokolu API, který zaznamená všechny zprávy API.
- **„Zahrnout tržní data do souboru protokolu API“** – zahrne všechna tržní data vrácená touto žádostí do protokolu.
- **„Úroveň protokolování“** je rozbalovací nabídka pro úpravu informací přítomných v protokolech. Pokud je toto nastaveno na nejvyšší úroveň nazvanou „Detail“, protokoly API zdokumentují veškerý provoz API do a z Trader Workstation.

Po povolení těchto nastavení mohou uživatelé kliknout na **Použít** a poté na **OK** dole, aby potvrdili a uložili tyto změny.

- [campus: What is the TWS API?](https://www.interactivebrokers.com/campus/trading-lessons/what-is-the-tws-api/)
- [campus: Installing & Configuring TWS for the API](https://www.interactivebrokers.com/campus/trading-lessons/installing-configuring-tws-for-the-api/)
- [campus: Accessing the TWS Python API Source Code](https://www.interactivebrokers.com/campus/trading-lessons/accessing-the-tws-python-api-source-code/)

### Placing Orders

- [campus: Placing Orders using TWS Python API](https://www.interactivebrokers.com/campus/trading-lessons/python-placing-orders/)
- [youtube: Placing Orders using TWS Python API](https://www.youtube.com/watch?v=vTXJ7v8ktis)