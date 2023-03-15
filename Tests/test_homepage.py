import pytest
from select import select
from selenium.webdriver.support.select import Select

from Testdata.test_homepagedata import Testhomepagedata
from Utilities.Baseclass import Baseclass
from homepageobject.homepage import homepage


class Testhomepage(Baseclass):
     def test_home1(self,getdata):
          log = self.getlogger()
          home=homepage(self.driver)
          home.name1().send_keys(getdata["firstname"])
          home.email1().send_keys(getdata["email"])
          home.password1().send_keys(getdata["Pwd"])
          home.checkbox1().click()
          self.visibletext(home.dropdown1(),getdata["gender"])
          home.radiobtn1().click()
          home.submitbtn1().click()
          alert=(home.sucmsg1().text)
          log.info(alert)
          assert ('Success!' in alert)

     #@pytest.fixture(params=Testhomepagedata.getTestdata("Test2"))
     @pytest.fixture(params=Testhomepagedata.data)
     def getdata(self,request):
          return request.param










