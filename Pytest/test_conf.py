import pytest

@pytest.mark.usefixtures("setup")
class Testexample:

    def test_firstprogram(self):
        print("hello")

    def test_firstprogram1(self):
        print("hello1")

    def test_firstprogram2(self):
        print("hello2")