# import time
# import random
#
# import pytest
# from selenium.common import NoSuchElementException
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

# from utilities.pageutils import PageUtils


class MattressPLP:

    FIRST_MATTRESS = (By.XPATH, "(//div[@class = 'plp-fragment-wrapper'])[1]")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def select_mattress(self):
        self.wait.until(self.ec.visibility_of_element_located(self.FIRST_MATTRESS)).click()
