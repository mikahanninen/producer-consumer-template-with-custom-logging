import logging
import os
from pathlib import Path
import sys


class CustomerLogging:
    def __init__(self):
        self.logger = logging.getLogger(__file__)
        self.logger.handlers = []
        self.log_filename = Path(
            os.getenv("ROBOT_ARTIFACTS", os.curdir), "customer.log"
        )
        fileout = logging.FileHandler(filename=self.log_filename)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        fileout.setFormatter(formatter)
        self.logger.addHandler(fileout)

    def customer_log(self, message: str):
        self.logger.info(message)
