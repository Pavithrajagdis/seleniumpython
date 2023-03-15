from selenium.webdriver.common.by import By

from Pageobject.Confirmpage import Confirmationpage


class Productpage:
    def __init__(self,driver):
        self.driver=driver

    text=(By.XPATH, "//td/div/div/h4/a")

    def text1(self):
        return self.driver.find_element(*Productpage.text)

    checkoutbutton=(By.XPATH, "//button[@class='btn btn-success']")

    def checkbutton1(self):
         self.driver.find_element(*Productpage.checkoutbutton).click()
         confirm = Confirmationpage(self.driver)
         return confirm


