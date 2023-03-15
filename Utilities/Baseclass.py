import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:
    def verifylinkpresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))

    def visibletext(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getlogger(self):
        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(loggername)         #loggername will give the method from which u r running the test.
        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)                 # filehandler object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger                  #logger is an object of logging

