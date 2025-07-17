import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    baseurl = "https://www.dutchbros.com/"

    # driver setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseurl)

    # Yield the driver for the test
    yield driver

    # After the test, close the browser
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
