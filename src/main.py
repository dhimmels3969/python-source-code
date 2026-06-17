from src import driver
import os
import sys
from pathlib import Path
from logging_config import setup_logging
import logging

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Application started")
    src_dir = Path(os.path.dirname(__file__))
    print()
    driver = driver.driver(src_dir.parent, sys.argv[1:])

    logger.info("Application ended.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
