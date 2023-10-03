import logging
import time
import os


class Logger(object):

    def __init__(self, log_level=logging.DEBUG):

        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        datetime_stamp = '%m/%d/%Y %I:%M:%S %p'
        format = logging.Formatter('%(asctime)s - %(filename)s : %(funcName)5s : [%(lineno)s] - %(message)s', datefmt=datetime_stamp)
        LogFileName = os.path.join(os.getcwd(), "Logs", "log.txt")

        fh = logging.FileHandler(filename=LogFileName)
        fh.setFormatter(format)
        fh.setLevel(log_level)
        self.logger.addHandler(fh)

    def _logger(self):
        return self.logger
