from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.ikea.com/us/en/")

wait = WebDriverWait(driver, 10)

# Step 1: Accept cookies if banner appears
try:
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]")))
    accept_button.click()
except:
    print("No cookie banner to accept.")

# Step 2: Click the hamburger menu ("Products" tab)
menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-controls = 'tab-products']")))
menu_button.click()

# Step 3: Click the "Outdoor" category in the left menu
outdoor_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav[@data-testid='hnf-menu-left-nav']//a[contains(text(), 'Outdoor')]")))
outdoor_link.click()

# Step 4: Click "Outdoor furniture" from the right side dropdown list
outdoor_furniture_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav[@data-testid='hnf-menu-right-nav']//a[contains(text(), 'Outdoor furniture')]")))
outdoor_furniture_link.click()
