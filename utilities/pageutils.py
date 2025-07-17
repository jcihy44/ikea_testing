import json
import os
import random
import secrets
import string
import time

# import allure
# from pytest_check import check
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

class PageUtils(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(self.driver)

    def click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_into_center(self, element):
        script = """
            var element = arguments[0];
            var rect = element.getBoundingClientRect();
            var x = (window.innerWidth - rect.width) / 2;
            var y = (window.innerHeight - rect.height) / 2;
            window.scrollTo(x, y);
        """
        self.driver.execute_script(script, element)

    def enter_text(self, element, text):
        """js executor method , alternative to selenium send keys"""
        self.driver.execute_script(f"arguments[0].value='{text}';", element)

    def highlight_element(self, element, color="#abdbe3"):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        border_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.driver.execute_script(
            f"arguments[0].setAttribute('style', 'background-color: {random_color}; border: 1px dotted {border_color}; border-style: "
            "inset');",
            element,
        )