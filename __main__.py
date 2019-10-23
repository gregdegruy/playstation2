#! /bin/python

import time

from classes import HDL

if __name__ == '__main__':
    print("Start: " + time.asctime( time.localtime(time.time()) ))
    hdd = ''
    isoFolder = ''
    hdlPath = ''
    hdl = HDL(hdd, isoFolder, hdlPath)
    print('HDL instance ' + hdl.__str__())
    print('Running...')
    # hdl.bulkInjectDvd()
    # hdl.saveGamesListToFile()
    print("End: " + time.asctime( time.localtime(time.time()) ))
    print('\nDone')
