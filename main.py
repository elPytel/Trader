import requests
import csv
from tabulate import tabulate
from basic_colors import *
from ibapi.client import *
from ibapi.wrapper import *
from decimal import Decimal

import logging
import colorama
from colorama import Fore, Style
colorama.init()

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.INFO: Fore.BLUE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
        logging.DEBUG: Fore.CYAN,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        levelname = f"{color}[{record.levelname}]{Style.RESET_ALL}"
        message = super().format(record)
        return message.replace(f"[{record.levelname}]", levelname)

console_formatter = ColoredFormatter("[%(levelname)s] %(message)s")
file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

handler_file = logging.FileHandler("trader.log", encoding="utf-8")
handler_console = logging.StreamHandler()

handler_file.setFormatter(file_formatter)
handler_console.setFormatter(console_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler_file, handler_console]
)

PAPER_TRADING_PORT = 7497
PORT = PAPER_TRADING_PORT

clientID = 100

HASH = None
with open(".hash", "r") as f:
    HASH = f.read().strip()

strategies = [
    "MondayBuyer",
    "SMRCA_L",
]

BASE_URL = "https://tradingroom.financnik.cz/download/"

def download_csv(base_url, strategy, hash_value):
    file_type = "csv"
    filename = f"{strategy}.{file_type}"
    url = f"{base_url}{strategy}/{file_type}/{hash_value}"
    response = requests.get(url)
    if response.status_code == 200:
        text = response.content
        logging.info(f"Staženo: {filename}")
        return text, filename
    else:
        logging.error(f"Chyba při stahování: {response.status_code}")
    return None, None

def save_to_file(text, filename):
    logging.info(f"Ukládám: {filename}")
    with open(filename, "wb") as f:
        f.write(text)

def load_csv_table(filename):
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        table = list(reader)
    logging.info(f"Nahráno: {filename} ({len(table)} řádků)")
    return table

def print_csv_table(table, columns=-1):
    rows = list(table)
    header = rows[0][0:columns]
    data = [row[0:columns] for row in rows[1:]]
    print(tabulate(data, headers=header, tablefmt="grid"))


"""
for strategy in strategies:
    text, filename = download_csv(BASE_URL, strategy, HASH)
    if text and filename:
        save_to_file(text, filename)
"""

print_csv_table(load_csv_table("SMRCA_L.csv"), 11)

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqContractDetails(orderId, mycontract)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(contractDetails.contract)

        myorder = Order()
        myorder.orderId = reqId
        myorder.action = "SELL"
        myorder.tif = "GTC"
        myorder.orderType = "LMT"
        myorder.lmtPrice = 144.80
        myorder.totalQuantity = 10

        self.placeOrder(myorder.orderId, contractDetails.contract, myorder)

    def openOrder(
        self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState
    ):
        print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")

    def orderStatus(
        self,
        orderId: OrderId,
        status: str,
        filled: Decimal,
        remaining: Decimal,
        avgFillPrice: float,
        permId: int,
        parentId: int,
        lastFillPrice: float,
        clientId: int,
        whyHeld: str,
        mktCapPrice: float,
    ):
        print(
            f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}"
        )

    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")


app = TestApp()
app.connect("127.0.0.1", PORT, clientID)
#app.run()
