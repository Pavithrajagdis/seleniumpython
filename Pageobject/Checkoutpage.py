from selenium.webdriver.common.by import By

from Pageobject.Productpage import Productpage


class Checkout:
    def __init__(self,driver):
        self.driver=driver

    phones=(By.XPATH, "//div[@class='card h-100']")

    def Phonetitle(self):
        return self.driver.find_elements(*Checkout.phones)     # driver is now class variable ,so we have self.driver

    button=(By.XPATH, "//button[@class='btn btn-info']")

    def button1(self):
        return self.driver.find_element(*Checkout.button)

    primarybutton=(By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def primbutton(self):
          self.driver.find_element(*Checkout.primarybutton).click()
          product = Productpage(self.driver)
          return product
