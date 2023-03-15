import pytest

from Pytest.BaselogClass import BaselogClass


@pytest.mark.usefixtures("dataload")
class TestData(BaselogClass):                        #inheriting the baseclass

    def test_fun2(self, dataload):
        log=self.getlogger()
        log.info(dataload)