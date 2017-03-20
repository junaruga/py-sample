import logging
import sys

if __name__ == '__main__':
    print('Start')
    logger = logging.getLogger('mylogger')
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug('Test string')
    print('End')
