from selenium.webdriver.common.by import By


class homepage:
    def __init__(self,driver):
        self.driver=driver

    name= (By.XPATH,"(//input[@name='name'])[1]")

    def name1(self):
        return self.driver.find_element(*homepage.name)

    email = (By.XPATH, "(//input[@name='email'])[1]")

    def email1(self):
        return self.driver.find_element(*homepage.email)

    password = (By.XPATH, "//input[@type='password']")

    def password1(self):
            return self.driver.find_element(*homepage.password)

    checkbox = (By.XPATH, "//input[@id ='exampleCheck1']")

    def checkbox1(self):
        return self.driver.find_element(*homepage.checkbox)

    dropdown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")

    def dropdown1(self):
        return self.driver.find_element(*homepage.dropdown)

    radiobtn = (By.XPATH, "(//input[@ type='radio'])[1]")

    def radiobtn1(self):
        return self.driver.find_element(*homepage.radiobtn)

    submitbtn = (By.XPATH, "//input[@ type='submit']")

    def submitbtn1(self):
        return self.driver.find_element(*homepage.submitbtn)

    sucmsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def sucmsg1(self):
        return self.driver.find_element(*homepage.sucmsg)
