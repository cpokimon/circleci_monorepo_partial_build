from time import sleep
from logging import getLogger

logger = getLogger()

while True:
    logger.warning('Service 2. Hello World! Edited')
    sleep(2)
