from time import sleep
from logging import getLogger

logger = getLogger()

while True:
    logger.warning('Service 1. Hello World!')
    sleep(1)
