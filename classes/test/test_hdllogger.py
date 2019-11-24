import logging
import os
import platform

from ..hdllogger import HDLLogger

className = 'HDLLogger'
logName = 'TEST.log'
logFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
subdir = ''
if platform.system() == 'Windows':
    subdir = 'classes\\test\\'
elif platform.system() == 'Linux':
    subdir = 'classes/test/'

def test_init():
    print('Call ' + className + '.test_init()')
    testLogger = HDLLogger(logName)
    assert testLogger.name == logName
    assert testLogger.logger.isEnabledFor(logging.DEBUG)
    assert testLogger.logger.handlers[0].formatter._fmt == logFormat

def test_log():
    print('Call ' + className + '.test_log()')
    testLogger = HDLLogger(logName, 'classes/test/')
    if os.path.isfile(testLogger.fileHandlerPath):
        f = open(testLogger.fileHandlerPath, 'r+')
        f.truncate(0)
    testLogger.log('Test')
    file = open(logName, 'r')
    lastLine = file.readlines()[-1]
    file.close()
    assert '- hdl_dump - INFO - Test\n' == lastLine[-25:]
