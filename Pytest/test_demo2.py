from Pytest.BaselogClass import BaselogClass


class Testdemo2(BaselogClass):
     def test_firstprogram1(self):
         log=self.getlogger()
         log.info("hello1")
    #print("hello1")