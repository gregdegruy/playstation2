import logging
import os
import platform

class HDLLogger():
    name = ''
    logger = logging.getLogger('hdl_dump')
    fileHandlerPath = ''

    def __init__(self, name, subdir=''):
        self.name = name
        self.logger.setLevel(logging.DEBUG)
        if platform.system() == 'Windows':
            self.fileHandlerPath = os.getcwd() + '\\' + subdir + name
        elif platform.system() == 'Linux':
            self.fileHandlerPath = os.getcwd() + '/' + subdir + name
        fh = logging.FileHandler(self.fileHandlerPath)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') )
        self.logger.addHandler(fh)

    def log(self, message):
        self.logger.info(message)
