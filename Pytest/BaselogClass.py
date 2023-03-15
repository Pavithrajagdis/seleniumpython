import inspect
import logging

class BaselogClass:

    def getlogger(self):
        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(loggername)         #loggername will give the method from which u r running the test.
        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)
        # filehandler object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        #logger.debug("a debug statement is executed")
        #logger.info("information")
        #logger.warning("alert:warning")
        #logger.error("error")
        #logger.critical("critical")
        return logger                  #logger is an object of logging

