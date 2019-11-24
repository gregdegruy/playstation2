#! /bin/python

import time
import os

from classes import HDL

if __name__ == '__main__':
    print('Start: ' + time.asctime( time.localtime(time.time()) ))
    hdd = 'hddx:'
    isoDirectoryPath = 'D:\\replace\\me\\myisofolder'
    hdlPath = 'C:\\replace\\me\\hdl_dump.exe'
    hdl = HDL(hdd, isoDirectoryPath, hdlPath)
    print('HDL instance\n' + hdl.__str__())
    print('Running...')
    # hdl.bulkInjectDvd()
    # hdl.bulkConvertBinToIso()
    # hdl.saveGamesListToFile()
    print('End: ' + time.asctime( time.localtime(time.time()) ))
    print('\nDone')
