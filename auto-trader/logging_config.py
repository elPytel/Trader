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

def configure_logging(level=logging.INFO, logfile="trader.log"):
    console_formatter = ColoredFormatter("[%(levelname)s] %(message)s")
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    handler_file = logging.FileHandler(logfile, encoding="utf-8")
    handler_console = logging.StreamHandler()

    handler_file.setFormatter(file_formatter)
    handler_console.setFormatter(console_formatter)

    root = logging.getLogger()
    # remove existing handlers to ensure predictable configuration
    if root.handlers:
        root.handlers.clear()

    root.setLevel(level)
    root.addHandler(handler_file)
    root.addHandler(handler_console)

# configure on import to preserve current behaviour in your main.py
configure_logging()