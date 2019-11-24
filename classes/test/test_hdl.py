import os
import platform
import subprocess
import sys

from ..hdl import HDL

className = 'HDL'
hdd = 'hddx:'
if platform.system() == 'Windows':
    isoDirectoryPath = os.getcwd() + '\\classes\\test\\games'
    hdlPath = os.getcwd() + '\\classes\\test\\games'
elif platform.system() == 'Linux':
    isoDirectoryPath = os.getcwd() + '/classes/test/games'
    hdlPath = os.getcwd() + '/classes/test/games'

def test_init():
    print('Call ' + className + '.test_init()')

    testHdl = HDL(hdd, isoDirectoryPath, hdlPath)
    print('HDL instance\n' + testHdl.__str__())
    assert testHdl.hdd == hdd
    assert testHdl.isoDirectoryPath == isoDirectoryPath
    assert testHdl.hdlPath == hdlPath

def test_format_slu():
    print('Call ' + className + '.test_format_slu()')
    serial = 'SLUS-21693 (1.03).iso'
    result = serial[:4] + "_" + serial[4 + 1:]
    result = result[:8] + "." + result[8:]
    result = result[0:11]
    assert result == 'SLUS_216.93'

def test_read_game_folder():
    print('Call ' + className + '.test_read_game_folder()')
    expectedGames = ['Game A (USA)', 'Game B (USA)', 'Game C (USA)', 'Game D (USA)', 'Game E (USA)']
    games = []
    gameName = 'undefined'
    try:
        for root, dirs, files in os.walk(isoDirectoryPath):
            for file in files:
                with open(os.path.join(root, file), 'r') as auto:
                    if platform.system() == 'Windows':
                        gameName = root.split('\\')[-1]
                    elif platform.system() == 'Linux':
                        gameName = root.split('/')[-1]
                    games.append(gameName)
    except OSError as e:
        print('OS error: {0}'.format(e))
    except:
        e = sys.exc_info()[0]
        print('Exception {0}'.format(e))
    finally:
        for i in range(0, 4):
            assert games[i] in expectedGames

def test_detect_bin_and_iso():
    print('Call ' + className + '.test_detect_bin_and_iso()')
    expectedIsos = ['SLUS-123456 (0.00).iso', 'SLUS-101010 (0.00).iso', 'SLUS-777888 (0.00).iso']
    expectedBins = ['SLUS-000000 (0.00).bin', 'SLUS-123000 (1.00).bin']
    isos = []
    bins = []
    gameName = 'undefined'
    try:
        for root, dirs, files in os.walk(isoDirectoryPath):
            for file in files:
                fileName = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                with open(os.path.join(root, file), 'r') as auto:
                    if extension == '.iso':
                        isos.append(file)
                    elif extension == '.bin':
                        bins.append(file)
    except OSError as e:
        print('OS error: {0}'.format(e))
    except:
        e = sys.exc_info()[0]
        print('Exception {0}'.format(e))
    finally:
        for iso in isos:
            assert iso in expectedIsos
        for bin in bins:
            assert bin in expectedBins
