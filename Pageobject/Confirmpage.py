from selenium.webdriver.common.by import By


class Confirmationpage:
    def __init__(self, driver):
       self.driver=driver

    Country= (By.XPATH, "//input[@id='country']")

    def Country1(self):
        return self.driver.find_element

    Purchase=(By.XPATH, "//input[@value='Purchase']")

    def Purchase1(self):
        return self.driver.find_element(*Confirmationpage.Purchase)

    Successmsg=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def Sucmsg(self):
        return self.driver.find_element(*Confirmationpage.Successmsg)