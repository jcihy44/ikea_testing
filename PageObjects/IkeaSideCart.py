# import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# from utilities.pageutils import PageUtils


class SideCart:
    def __init__(self, driver):
        self.driver = driver
        # self.utils = PageUtils(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.ec = ec

    CONTINUE_SHOPPING = (By.XPATH, "//span[contains(text(),'Continue shopping')]")
    GO_TO_SHOPPING_BAG = (By.XPATH, "//button//span[contains(text(),'Go to shopping bag')]")

    def continue_shopping(self):
        button_continue_shopping = self.driver.find_element(*self.CONTINUE_SHOPPING)
        button_continue_shopping.click()

    def go_to_shopping_bag(self):
        # button_go_to_cart = self.driver.find_element(*self.CONTINUE_SHOPPING)
        # button_go_to_cart.click()
        self.wait.until(self.ec.visibility_of_element_located(self.GO_TO_SHOPPING_BAG)).click()