#! /bin/python

import time
import os

from classes import HDL

if __name__ == '__main__':
    print('Start: ' + time.asctime( time.localtime(time.time()) ))
    hdd = ''
    isoDirectoryPath = ''
    hdlPath = ''
    hdl = HDL(hdd, isoDirectoryPath, hdlPath)
    print('HDL instance\n' + hdl.__str__())
    print('Running...')
    # hdl.bulkInjectDvd()
    # hdl.saveGamesListToFile()
    print('End: ' + time.asctime( time.localtime(time.time()) ))
    print('\nDone')
