import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Pageobject.Checkoutpage import Checkout
from Pageobject.Confirmpage import Confirmationpage
from Pageobject.Homepage import Homepage
from Pageobject.Productpage import Productpage
from Utilities.Baseclass import Baseclass


#@pytest.mark.usefixtures("setup")
class Testone(Baseclass):
    def test_e2e(self):
        log=self.getlogger()        #the methods on baseclass can be called [self.methodname]
        homepage= Homepage(self.driver)
        checkout=homepage.shopitem()   #here shopitem method will retuen checkout object as a return type
        phones=checkout.Phonetitle()

        for x in phones:

            phonetitle = x.find_element(By.XPATH, "//div/h4/a").text
            if phonetitle == "iphone X":
                checkout.button1().click()
            else:
                continue
        product=checkout.primbutton()

        log.info(product.text1().text)

        confirm=product.checkbutton1()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
        self.verifylinkpresence("India")    #call method from base class with self object
        confirm.Purchase1().click()
        sucessmessage = confirm.Sucmsg().text
        log.info(sucessmessage)

        assert 'Success! Thank you!' in sucessmessage


