import logging
import time
import os


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        format = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        current_time = time.strftime("%Y-%m-%d")
        self.LogFileName = os.path.join(os.getcwd, "Logs", "log", current_time, ".txt")
        filehandler = logging.FileHandler(self.LogFileName, mode="a")
        filehandler.setFormatter(format)
        filehandler.setLevel(file_level)
        self.logger.addHandler(filehandler)
