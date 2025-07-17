import time
import random

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


# from utilities.pageutils import PageUtils


class ShopifyNav:

    IKEA_LOGO = (By.XPATH, "//img[@src = 'https://www.ikea.com/global/assets/logos/brand/ikea.svg']")
    SEARCH = (By.XPATH, "//input[@type = 'search']")
    CART = (By.XPATH, "//div[@class = 'hnf-header__shopping-cart-link']")
    FAVORITES = (By.XPATH, "//span[contains(text(),'Favorites')]")
    ACCOUNT = (By.XPATH, "//div[@id = 'hnf-header-profile']")
    LOCATION = (By.XPATH, "//div[@id = 'hnf-header-storepicker']")
    REGION =
    LANGUAGE

    PRODUCTS = (By.XPATH, "//button[@aria-controls = 'tab-products']")
    ROOMS = (By.XPATH, "//button[@aria-controls = 'tab-rooms']")
    DEALS = (By.XPATH, "//button[@aria-controls = 'tab-offers']")
    COLLEVE_ESSENTIALS = (By.XPATH, "//button[@aria-controls = 'tab-starting-college']")
    HOME_ACCESSORIES = (By.XPATH, "//button[@aria-controls = 'tab-shop-marketplace-pub0a505b20']")
    IDEAS_INSPIRATION = (By.XPATH, "//button[@aria-controls = 'tab-ideas']")
    DESIGN_PLANNING = (By.XPATH, "//button[@aria-controls = 'tab-planners']")
    IKEA_FOR_BUSINESS = (By.XPATH, "//button[@aria-controls = 'tab-ikea-business']")
    SERVICES_SUPPORT = (By.XPATH, "//button[@aria-controls = 'tab-services']")

