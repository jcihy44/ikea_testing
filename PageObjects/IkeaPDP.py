import time
import random

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

# from utilities.pageutils import PageUtils


class IndividualPDP:

    SELECT_SIZE = (By.XPATH, "//button[@aria-controls = 'pip-product-variation-size']")
    SELECT_QTY = (By.XPATH, "//input[@inputmode = 'numeric']")
    ADD_TO_BAG = (By.XPATH, "//div[@class = 'pip-buy-module__buy-button-container ']//button[@aria-label = 'Add to bag']")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def select_qty(self, qty=1):
        qty_button = WebDriverWait(self.driver, 10).until(
            self.ec.visibility_of_element_located(self.SELECT_QTY)
        )
        for _ in range(qty - 1):
            qty_button.click()

    def add_to_bag(self):
        self.driver.find_element(*self.ADD_TO_BAG).click()
