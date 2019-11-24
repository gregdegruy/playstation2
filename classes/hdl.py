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

    def formatSerialNumberName(self, serial):
        result = serial[:4] + "_" + serial[4 + 1:]
        result = result[:8] + "." + result[8:]
        return result[0:11]

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

    def bulkConvertBinToIso(self):
        self.logger.log('HDL.bulkInjectDvd() Called')
        hdlCommand = 'inject_dvd'
        gameName = 'undefined'
        try:
            for root, dirs, files in os.walk(self.isoDirectoryPath):
                for file in files:
                    fileName = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.7z':
                        command = 'del "' + root + '\\' + file  + '"'
                        print('Archive clean up: ' + file + ' deleted')
                        self.logger.log('Archive clean up: ' + file + ' deleted')
                    else:
                        with open(os.path.join(root, file), 'r') as auto:
                            gameName = root.split('\\')[-1]
                            if extension == '.bin':
                                command = 'D:\\ApplicationFiles\\AnyToISO\\anytoiso /convert ' \
                                    + '"' + root + '\\' + fileName + '.bin' + '" ' \
                                    + '"' + root + '\\' + fileName + '.iso' + '"'
                                procOutput = subprocess.getoutput(command)
                                print('Convert: {0} {1} to .iso'.format(gameName, file))
                                self.logger.log('Convert: {0} {1} to .iso'.format(gameName, file))
        except OSError as e:
            print('OS error: {0}'.format(e))
            self.logger.log('OS error: {0} for game {1}'.format(e, gameName))
        except:
            e = sys.exc_info()[0]
            print('Exception {0}'.format(e))
            self.logger.log('Exception {0} for game {1}'.format(e, gameName))
        finally:
            self.logger.log('HDL.bulkInjectDvd() Terminated')

    # example command -> hdl_dump.exe inject_dvd hdd2: "Game Name (USA)" "C:\path\game.iso" SLUS_212.05 *u4
    def bulkInjectDvd(self):
        self.logger.log('HDL.bulkInjectDvd() Called')
        hdlCommand = 'inject_dvd'
        gameName = 'undefined'
        try:
            for root, dirs, files in os.walk(self.isoDirectoryPath):
                for file in files:
                    fileName = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.7z':
                        command = 'del "' + root + '\\' + file  + '"'
                        # subprocess.call(command)
                        print('Archive clean up: ' + file + ' deleted')
                        self.logger.log('Archive clean up: ' + file + ' deleted')
                    else:
                        with open(os.path.join(root, file), 'r') as auto:
                            gameName = root.split('\\')[-1]
                            if extension == '.iso':
                                slu = 'XXXX_XXX.XX'
                                slu = self.formatSerialNumberName(fileName)
                                command = self.hdlPath + ' ' + hdlCommand  + ' ' \
                                    + self.hdd + ' "' + gameName + '" ' + '"' + root + '\\' \
                                    + file + '" ' + slu + ' ' + self.sliceIndex
                                procOutput = '<' + hdlCommand + ' not called>'
                                # uncomment when ready for loading
                                # subprocess.call(command)
                                self.logger.log('Inject: ' + gameName + ' complete')
                                print('Inject: ' + gameName + ' complete')
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
