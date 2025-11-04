import requests
import csv
from tabulate import tabulate
import logging

logger = logging.getLogger(__name__)

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
        logging.error(f"Chyba: {response.status_code} při stahování: {filename}")
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

if __name__ == "__main__":

    for strategy in strategies:
        text, filename = download_csv(BASE_URL, strategy, HASH)
        if text and filename:
            save_to_file(text, filename)
            print_csv_table(load_csv_table(filename), 11)


    #print_csv_table(load_csv_table("SMRCA_L.csv"), 11)