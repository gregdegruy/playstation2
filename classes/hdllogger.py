import logging
import os

class HDLLogger():
    name = ''
    logger = logging.getLogger('hdl_dump')

    def __init__(self, name):
        self.name = name
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.getcwd() + '\\' + name)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') )
        self.logger.addHandler(fh)

    def log(self, message):
        self.logger.info(message)
