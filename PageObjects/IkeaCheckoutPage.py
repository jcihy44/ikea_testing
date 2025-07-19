import time
import random
import string

# import allure
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from utilities.takescreenshotevents import takeScreenshot
from selenium.webdriver import ActionChains

# from utilities.pageutils import PageUtils

#  to be changed when using for testing and not just a single email
# def generate_email():
#     prefix = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
#     return f"{prefix}@gmail.com"

class IkeaCheckout:
    def __init__(self, driver):
        self.string = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        # self.utils = PageUtils(self.driver)
        self.ec = ec


    CONTINUE_TO_CHECKOUT = (By.XPATH, "//button//span[@class =  contains(text(),'Continue to checkout')]")
    CONTINUE_AS_GUEST = (By.XPATH, "//button//span[@class =  contains(text(),'Continue as guest')]")
    JOIN_OR_LOGIN = (By.XPATH, "//button//span[@class =  contains(text(),'Join for free or log in')]")
    ZIP_CODE = (By.ID, "zipInInput")
    PICK_UP = (By.XPATH, "//button[@class = 'order-capture-web__choice-item__action']")
    CONTINUE_TO_DETAILS = (By.XPATH, "//button[contains(., 'Continue')]")
    EMAIL = (By.ID, "REGULAR-billing-email")
    PHONE = (By.ID, "REGULAR-billing-mobileNumber")
    FIRST_NAME = (By.ID, "REGULAR-billing-firstName")
    LAST_NAME = (By.ID, "REGULAR-billing-lastName")
    ADDRESS_LINE1 = (By.ID, "REGULAR-billing-addressLine1")
    ADDRESS_LINE2 = (By.ID, "REGULAR-billing-addressLine2")
    POSTALCODE = (By.ID, "REGULAR-billing-zipCode")
    CITY = (By.ID, "REGULAR-billing-city")
    STATE = (By.ID, "REGULAR-billing-stateCode")
    CONTINUE_TO_PAYMENT = (By.XPATH, "//button[@type = 'submit']//span[@class  = contains(text(),'Continue')]")



    # to be changed when using for testing and not just a single email
    # email = generate_email()

    email = "jcihy4test@gmail.com"

    ADDRESSES = {
        # "CA": {
        #     "email": f"{email}",
        #     "first_name": "shipx",
        #     # "last_name": f"{string}",
        #     "address": "78 Overton Crescent",
        #     "city": "Toronto",
        #     "state": "Ontario",
        #     "postal_code": "M3B 2V2",
        #     "phone": f"4245584331",
        # },
        "US": {
            "email": f"{email}",
            "first_name": "shipx",
            # "last_name": f"{string}",
            "address": "3717 Leisure Lane",
            "city": "Simi Valley",
            "state": "California",
            "postal_code": "93065",
            "phone": "4245484331",
        },
        # "UK": {
        #     "email": f"{email}",
        #     "first_name": "shipx",
        #     # "last_name": f"{string}",
        #     "address": "49 Featherstone Street",
        #     "city": "LONDON",
        #     "state": "	UNITED KINGDOM",
        #     "postal_code": "EC1Y 8SY",
        #     "phone": "01753832233",
        # }
    }

    def cont_to_checkout(self):
        self.wait.until(self.ec.visibility_of_element_located(self.CONTINUE_TO_CHECKOUT)).click()

    def cont_as_guest(self):
        self.wait.until(self.ec.visibility_of_element_located(self.CONTINUE_AS_GUEST)).click()

    def input_zip(self):
        # zip = self.wait.until(self.ec.visibility_of_element_located(self.ZIP_CODE))
        # zip.click()
        # zip.send_keys("85048")

        zip_input = self.wait.until(ec.presence_of_element_located((By.ID, "zipInInput")))
        zip_input.clear()
        zip_input.send_keys("85048")  # Use a valid zip code
        zip_input.send_keys(Keys.RETURN)
        time.sleep(5)
    def cont_to_details(self):
        self.wait.until(self.ec.element_to_be_clickable(self.CONTINUE_TO_DETAILS)).click()
    def pick_up(self):
        self.wait.until(self.ec.visibility_of_element_located(self.PICK_UP)).click()

    # def cont_to_details(self):
    #     el = self.wait.until(self.ec.visibility_of_element_located(self.CONTINUE_TO_DETAILS)).click()
    #     print(el.text)
    #     el.click()
    def cont_to_details(self):
        continue_button = self.wait.until(self.ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]")))
        continue_button.click()
        # button = self.driver.find_element(By.XPATH, ":(//button)[34]")
        # self.driver.execute_script("arguments[0].click();", button)
        # button = self.driver.find_element(By.XPATH, "//button[text()='Continue']")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(button).click().perform()

    def generate_string(self):
        prefix = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        return prefix

    def fillout_address_form(self, country=None, name=None):
        wait = WebDriverWait(self.driver, 10)

        if country in self.ADDRESSES:
            address_data = self.ADDRESSES[country]

        #fill out email field
        email_field = wait.until(ec.element_to_be_clickable(self.EMAIL))
        email_field.click()
        email_field.send_keys(self.email)

        # Fill out first name
        first_name_field = wait.until(ec.element_to_be_clickable(self.FIRST_NAME))
        first_name_field.click()
        if name is not None:
            first_name_field.send_keys(name)
        else:
            first_name_field.send_keys(address_data["first_name"])
        last_name_field = wait.until(ec.element_to_be_clickable(self.LAST_NAME))

        # fill out last name
        last_name_field.click()
        self.string = self.generate_string()
        last_name_field.send_keys(self.string)

        #fill out addressline 1
        address1_field = wait.until(ec.element_to_be_clickable(self.ADDRESS_LINE1))
        address1_field.click()
        address1_field.send_keys(address_data["address"])
        address1_field.send_keys(Keys.RETURN)

        #fill out city
        city_field = wait.until(ec.element_to_be_clickable(self.CITY))
        city_field.click()
        city_field.send_keys(address_data["city"])

        #fill out postal code
        postal_code_field = wait.until(ec.element_to_be_clickable(self.POSTALCODE))
        postal_code_field.click()
        postal_code_field.send_keys(address_data["postal_code"])

        postal_code_field = wait.until(ec.element_to_be_clickable(self.PHONE))
        postal_code_field.click()
        postal_code_field.send_keys(address_data["phone"])
        takeScreenshot(self.driver)

        state_dropdown = wait.until(ec.element_to_be_clickable(self.STATE)).click()
        select = Select(state_dropdown)
        select.select_by_visible_text("Ontario")



