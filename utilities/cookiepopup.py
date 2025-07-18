from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.ikea.com")

try:
    # Wait for the cookie modal and click "Accept all" (button text may vary by region/language)
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]"))
    )
    accept_button.click()
    print("Cookie modal closed.")
except Exception as e:
    print("No cookie modal found or failed to close:", e)

# Continue with the rest of your script...
