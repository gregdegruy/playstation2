import os
import subprocess
import sys

from .hdllogger import HDLLogger

class HDL:
    hdd = ''
    isoDirectoryPath = ''
    hdlPath = ''
    hdlCommand = ''
    sliceIndex = '*u4'
    logger = HDLLogger('LOG.log')

    def __init__(self, hdd, isoDirectoryPath, hdlPath):
        self.hdd = hdd
        self.hdlPath = hdlPath
        self.isoDirectoryPath = isoDirectoryPath

    # example input -> "SLUS-21693 (1.03).iso" output "SLUS_216.93"
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
            outs, errs = p.communicate(timeout=60)
            self.logger.log('Saved games list for {0}'.format(self.hdd))
        except TimeoutExpired:
            p.kill()
            outs, errs = p.communicate()
            self.logger.log('Saved games list for {0} failed with error {1}'.format(self.hdd, errs))

    # example command -> hdl_dump.exe inject_dvd hdd2: "Game Name (USA)" "C:\path\game.iso" SLUS_212.05 *u4
    def bulkInjectDvd(self):
        self.logger.log('HDL.bulkInjectDvd() Called')
        hdlCommand = 'inject_dvd'
        gameName = 'undefined'
        try:
            for root, dirs, files in os.walk(self.isoDirectoryPath):
                for file in files:
                    with open(os.path.join(root, file), 'r') as auto:
                        fileName = os.path.splitext(file)[0]
                        extension = os.path.splitext(file)[1]
                        gameName = root.split('\\')[-1]
                        # todo do not run bin to iso convert if an iso is in file collection
                        # ['18 Wheeler - Americ... (USA).7z', 'SLUS-20210 (1.00).bin', 'SLUS-20210 (1.00).iso']
                        if extension == '.iso':
                            slu = 'XXXX_XXX.XX'
                            slu = self.formatSerialNumberName(fileName)
                            command = self.hdlPath + ' ' + hdlCommand  + ' ' \
                                + self.hdd + ' "' + gameName + '" ' + '"' + root + '\\' \
                                + file + '" ' + slu + ' ' + self.sliceIndex
                            procOutput = '<' + hdlCommand + ' not called>'
                            # uncomment when ready for loading
                            # procOutput = subprocess.getoutput(command)
                            print('Inject {0} resulted in: '.format(gameName) + procOutput)
                            # self.logger.log('Inject {0} resulted in: '.format(gameName) + procOutput)
                        elif extension == '.bin':
                            command = 'D:\\ApplicationFiles\\AnyToISO\\anytoiso /convert ' \
                                + '"' + root + '\\' + fileName + '.bin' + '" ' \
                                + '"' + root + '\\' + fileName + '.iso' + '"'
                            procOutput = subprocess.getoutput(command)
                            # anytoiso /convert "SLUS-20210 (1.00).bin" "SLUS-20210 (1.00).iso"
                            print('Extension error: ' + gameName + ' ' + file + ' is a .bin need a .iso')
                            # self.logger.log('Extension error: {0} {1} is a .bin need a .iso'.format(gameName, file))
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
        return '{ hdd: "' + self.hdd + '", isoDirectoryPath: "' + self.isoDirectoryPath +  '", hdlPath: "' + self.hdlPath + '" }'
