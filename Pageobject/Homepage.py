from selenium.webdriver.common.by import By

from Pageobject.Checkoutpage import Checkout


class Homepage:
    def __init__(self, driver):
        self.driver=driver


    shop=(By.XPATH,"//a[text()='Shop']")

    def shopitem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkout = Checkout(self.driver)
        return checkout
