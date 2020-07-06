import pytest
from selenium import webdriver
from configparser import ConfigParser

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    global driver

    config = ConfigParser()
    config.read('..\\TestCases\\pytest.ini')
    browser = config.get('pytest', 'browser')
    url = config.get('pytest', 'url')

    #   To use browser from command line comment the above browser variable and uncomment the below variable
    #   browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="..//Drivers//chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="..//Drivers//geckodriver.exe")
    elif browser == "ie":
        driver = webdriver.Ie(executable_path="..//Drivers//IEDriverServer.exe")
    elif browser == "edge":
        driver = webdriver.Edge(executable_path="..//Drivers//msedgedriver.exe")

    driver.maximize_window()

    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()
