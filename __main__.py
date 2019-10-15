#! /bin/python

import time

from classes import HDL

if __name__ == '__main__':
    print("Start time: " + time.asctime( time.localtime(time.time()) ))
    # example
    # hdl = HDL('hdd2:', 'test', 'D:\path\hdl_dumx_rev47\hdl_dump.exe')
    hdl = HDL('HDD_NAME', 'ISO_FOLDER_NAME', 'PATH_TO_HDL_DUMP_EXE')
    print('HDL instance ' + hdl.__str__())
    print('Adding ISOs...')
    hdl.bulkInjectDvd()
    print("End time: " + time.asctime( time.localtime(time.time()) ))
    print('\nDone')
