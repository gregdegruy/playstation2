import os
import subprocess
import sys

from .hdllogger import HDLLogger

class HDL:
    hdd = ''
    isoFolder = ''
    hdlPath = ''
    hdlCommand = ''
    sliceIndex = '*u4'
    logger = HDLLogger('LOG.log')

    def __init__(self, hdd, isoFolder, hdlPath):
        self.hdd = hdd
        self.hdlPath = hdlPath
        self.isoFolder = isoFolder

    # example input "SLUS-21693 (1.03).iso" output "SLUS_216.93"
    def formatSerialNumberName(self, serial):
        result = serial[:4] + "_" + serial[4 + 1:]
        result = result[:8] + "." + result[8:]
        return result

    def saveGamesListToFile(self):
        hdlCommand = 'hdl_toc'
        file = self.hdd[:-1] + '_games.txt'
        command = self.hdlPath + ' ' + hdlCommand + ' ' + self.hdd + ' > ' + file
        os.system(command)
        p = subprocess.Popen(command, shell=True)
        try:
            outs, errs = p.communicate(timeout=30)
            self.logger.log('Saved games list for {0}'.format(self.hdd))
        except TimeoutExpired:
            p.kill()
            outs, errs = p.communicate()
            self.logger.log('Saved games list for {0} failed with error {1}'.format(self.hdd, errs))

    # example hdl_dump.exe inject_dvd hdd2: "Game Name (USA)" "C:\path\game.iso" SLUS_212.05 *u4
    def bulkInjectDvd(self):
        self.logger.log('HDL.bulkInjectDvd() Called')
        hdlCommand = 'inject_dvd'
        isoDirectory = os.getcwd() + '\\' + self.isoFolder
        gameName = 'undefined'
        try:
            for root, dirs, files in os.walk(isoDirectory):
                for file in files:
                    with open(os.path.join(root, file), 'r') as auto:
                        fileName = os.path.splitext(file)[0]
                        extension = os.path.splitext(file)[1]
                        if extension == '.iso':
                            slu = 'XXXX_XXX.XX'
                            slu = self.formatSerialNumberName(fileName)
                            gameName = root.split('\\')[-1]
                            command = self.hdlPath + ' ' + hdlCommand  + ' ' \
                                + self.hdd + ' "' + gameName + '" ' + '"' + root + '\\' \
                                + file + '" ' + slu + ' ' + self.sliceIndex
                            # uncommnet me when ready for loading
                            # subprocess.call(command)
                            self.logger.log('{0} Loaded'.format(gameName))
                        elif extension == '.bin':
                            print('Extension error: ' + file + ' is Not an iso')
                            self.logger.log('Extension error: {0} is Not an iso'.format(file))
        except OSError as e:
            print('OS error: {0}'.format(e))
            self.logger.log('OS error: {0} for game {1}'.format(e, gameName))
        except:
            e = sys.exc_info()[0]
            print('Exception {0}'.format(e))
            self.logger.log('Exception {0} for game {1}'.format(e, gameName))
        finally:
            self.logger.log('HDL.bulkInjectDvd() Terminated')

    def __str__(self):
        return '{ hdd: "' + self.hdd + '", hdlPath: "' + self.hdlPath + '" }'
