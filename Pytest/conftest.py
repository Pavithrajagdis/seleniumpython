import pytest


@pytest.fixture(scope="class")
def setup():
  print("first")
  yield
  print("last")

@pytest.fixture()
def dataload():
  print("ABC")
  return["pavi","thra"]

@pytest.fixture(params=[("chrome","pavi"),("firefox","thra"),("IE","Anv")])
def crossbrowser(request):                                    #request is a instance of a fixture
  return  request.param
