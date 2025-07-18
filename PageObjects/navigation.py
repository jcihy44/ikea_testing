import time
import random

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


# from utilities.pageutils import PageUtils


class IkeaTopNav:

    IKEA_LOGO = (By.XPATH, "//img[@src = 'https://www.ikea.com/global/assets/logos/brand/ikea.svg']")
    SEARCH = (By.XPATH, "//input[@type = 'search']")
    CART = (By.XPATH, "//div[@class = 'hnf-header__shopping-cart-link']")
    FAVORITES = (By.XPATH, "//span[contains(text(),'Favorites')]")
    ACCOUNT = (By.XPATH, "//div[@id = 'hnf-header-profile']")
    LOCATION = (By.XPATH, "//div[@id = 'hnf-header-storepicker']")
    REGION = (By.XPATH, "hnf-header-localisationpicker")
    GO_SHOPPING = (By.XPATH, "//section[@class = 'hero svelte-17ufdw2']//span[@class = contains(text(),'Go Shopping')]")
    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_home_page(self):
        self.wait.until(self.ec.visibility_of_element_located(self.IKEA_LOGO)).click()

    def nav_to_search(self):
        self.wait.until(self.ec.visibility_of_element_located(self.SEARCH)).click()

    def nav_to_cart(self):
        self.wait.until(self.ec.visibility_of_element_located(self.CART)).click()

    def nav_to_favorites(self):
        self.wait.until(self.ec.visibility_of_element_located(self.FAVORITES)).click()

    def nav_to_my_account(self):
        self.wait.until(self.ec.visibility_of_element_located(self.ACCOUNT)).click()

    def nav_to_my_location(self):
        self.wait.until(self.ec.visibility_of_element_located(self.LOCATION)).click()

    def nav_to_my_region(self):
        self.wait.until(self.ec.visibility_of_element_located(self.REGION)).click()

    def go_shopping(self):
        self.wait.until(self.ec.visibility_of_element_located(self.GO_SHOPPING)).click()

    def close_cookie_modal(self):
        try:
            # Wait for the cookie modal and click "Accept all" (button text may vary by region/language)
            accept_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]"))
            )
            accept_button.click()
            print("Cookie modal closed.")
        except Exception as e:
            print("No cookie modal found or failed to close:", e)

    def close_mini_cookie_modal(self):
        try:
            # Wait for the cookie modal and click "Accept all" (button text may vary by region/language)
            ok_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Ok')]"))
            )
            ok_button.click()
            print("Mini Cookie modal closed.")
        except Exception as e:
            print("Mini cookie modal not found or failed to close:", e)
class IkeaTabNav:

    PRODUCTS = (By.XPATH, "//button[@aria-controls = 'tab-products']")
    ROOMS = (By.XPATH, "//button[@aria-controls = 'tab-rooms']")
    DEALS = (By.XPATH, "//button[@aria-controls = 'tab-offers']")
    COLLEGE_ESSENTIALS = (By.XPATH, "//button[@aria-controls = 'tab-starting-college']")
    HOME_ACCESSORIES = (By.XPATH, "//button[@aria-controls = 'tab-shop-marketplace-pub0a505b20']")
    IDEAS_INSPIRATION = (By.XPATH, "//button[@aria-controls = 'tab-ideas']")
    DESIGN_PLANNING = (By.XPATH, "//button[@aria-controls = 'tab-planners']")
    IKEA_FOR_BUSINESS = (By.XPATH, "//button[@aria-controls = 'tab-ikea-business']")
    SERVICES_SUPPORT = (By.XPATH, "//button[@aria-controls = 'tab-services']")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_products(self):
        self.wait.until(self.ec.visibility_of_element_located(self.PRODUCTS)).click()

    def nav_to_rooms(self):
        self.wait.until(self.ec.visibility_of_element_located(self.ROOMS)).click()

    def nav_to_deals(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DEALS)).click()

    def nav_to_college_essentials(self):
        self.wait.until(self.ec.visibility_of_element_located(self.COLLEGE_ESSENTIALS)).click()

    def nav_to_home_accessories(self):
        self.wait.until(self.ec.visibility_of_element_located(self.HOME_ACCESSORIES)).click()

    def nav_to_ideas_inspiration(self):
        self.wait.until(self.ec.visibility_of_element_located(self.IDEAS_INSPIRATION)).click()

    def nav_to_design_planning(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DESIGN_PLANNING)).click()

    def nav_to_ikea_for_business(self):
        self.wait.until(self.ec.visibility_of_element_located(self.IKEA_FOR_BUSINESS)).click()

    def nav_to_services_support(self):
        self.wait.until(self.ec.visibility_of_element_located(self.SERVICES_SUPPORT)).click()

class CatagoryNav:

    NEW_TRENDING = (By.XPATH, "//a[@data-idx = '1']")
    OFFERS = (By.XPATH, "//a[@data-idx = '2']")
    STOREAGE_ORGANIZATION = (By.XPATH, "//a[@data-idx = '3']")
    SOFA_ARMCHAIRS = (By.XPATH, "//a[@data-idx = '4']")
    OUTDOOR = (By.XPATH, "//a[@data-idx = '5']")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_newtrending(self):
        self.wait.until(self.ec.visibility_of_element_located(self.NEW_TRENDING)).click()

    def nav_to_offers(self):
        self.wait.until(self.ec.visibility_of_element_located(self.OFFERS)).click()

    def nav_to_storeage_organization(self):
        self.wait.until(self.ec.visibility_of_element_located(self.STOREAGE_ORGANIZATION)).click()

    def nav_to_sofa_amchairs(self):
        self.wait.until(self.ec.visibility_of_element_located(self.SOFA_ARMCHAIRS)).click()

    def nav_to_outdoor(self):
        self.wait.until(self.ec.visibility_of_element_located(self.OUTDOOR)).click()

class DropdownNav:

    DROPDOWN_CAT1 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[1]//a")
    DROPDOWN_CAT2 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[2]//a")
    DROPDOWN_CAT3 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[3]//a")
    DROPDOWN_CAT4 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[4]//a")
    DROPDOWN_CAT5 = (By.XPATH, "//ul[@class = 'hnf-dropdown__column']//a[contains(text(),'Outdoor patio furniture')]")
    DROPDOWN_CAT6 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[6]")
    DROPDOWN_CAT7 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[7]")
    DROPDOWN_CAT8 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[8]")
    DROPDOWN_CAT9 = (By.XPATH, "(//ul[@class = 'hnf-dropdown__column']//li)[9]")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_dropdown_cat1(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT1)).click()

    def nav_to_dropdown_cat2(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT2)).click()

    def nav_to_dropdown_cat3(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT3)).click()

    def nav_to_dropdown_cat4(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT4)).click()

    # def nav_to_dropdown_cat5(self):
    #     self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT5)).click()

    def nav_to_dropdown_cat5(self):
        menu = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@role ='listbox']"))
        )
        ActionChains(self.driver).move_to_element(menu)
        wait_dropdown_cat5 = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.DROPDOWN_CAT5))
        wait_dropdown_cat5.click()

        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT5)).click()


    def nav_to_dropdown_cat6(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT6)).click()

    def nav_to_dropdown_cat7(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT7)).click()

    def nav_to_dropdown_cat8(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT8)).click()

    def nav_to_dropdown_cat9(self):
        self.wait.until(self.ec.visibility_of_element_located(self.DROPDOWN_CAT9)).click()

class RoomSlider:

    BEDROOM = (By.XPATH, "(//div[@id ='hnf-carousel__tabs-navigation-rooms']//span)[1]")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_bedroom(self):
        self.wait.until(self.ec.visibility_of_element_located(self.BEDROOM)).click()

class BedMatressSlider:

    MATTRESSES = (By.XPATH, "//a[@data-category-id = 'bm002']")

    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    def nav_to_mattresses(self):
        self.wait.until(self.ec.visibility_of_element_located(self.MATTRESSES)).click()
