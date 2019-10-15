import logging
import os

class HDLLogger():
    logger = logging.getLogger('hdl_dump')

    def __init__(self):
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.getcwd() + '\\LOG.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') )
        self.logger.addHandler(fh)

    def log(self, message):
        self.logger.info(message)