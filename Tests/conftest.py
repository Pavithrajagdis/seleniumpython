import pytest
from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

def pytest_addoption(parser):               #code to run in command prompt
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name== "chrome":
        service_obj = Service(
        r"C:\Users\pavij\chromedriver.exe")  # r ->coverts normal string to raw string.   #.exe extension is must in windows
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":
        service_obj = Service(
            r"C:\\Users\\pavij\\geckodriver-v0.32.2-win32.exe")
        driver=webdriver.Firefox(service=service_obj)
    elif browser_name=="IE":
        print("IE")
        service_obj = Service(
            r"C:\Users\pavij\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(
        "https://rahulshettyacademy.com/angularpractice/")
    driver.title
    request.cls.driver=driver         #here cls.driver =>driver of class which uses fixture. so we are assigning the driver in                                  #fixture class to the actual class driver which uses this fixture.
    yield
    driver.close()

