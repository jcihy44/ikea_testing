from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    # Step 1: Go to IKEA US homepage
    driver.get("https://www.ikea.com/us/en")

    # Step 2: Accept cookies if shown
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    except:
        pass  # Sometimes not shown

    # Step 3: Search for a product
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.send_keys("chair")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Click on first product
    product = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'plp-mastercard__item plp-mastercard__image ']")))
    product.click()

    # Step 5: Click "Add to bag"
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to bag')]")))
    add_to_cart.click()

    # Step 6: Click "Go to bag"
    # go_to_bag = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Go to bag')]")))
    # go_to_bag.click()

    # Step 7: Click "Checkout"
    checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[contains(text(),'Go to shopping bag')]")))
    checkout_button.click()
    time.sleep(5)

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button//span[@class =  contains(text(),'Continue to checkout')]")))
    checkout_button.click()
    time.sleep(5)

    # Step 8: Continue as guest
    continue_as_guest = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue as guest')]")))
    continue_as_guest.click()
    time.sleep(5)

    # Step 9: Enter ZIP code
    zip_input = wait.until(EC.presence_of_element_located((By.ID, "zipInInput")))
    zip_input.clear()
    zip_input.send_keys("85048")  # Use a valid zip code
    zip_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Step 10: Continue to delivery options
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]")))
    continue_button.click()

    # Step 11: Wait for address page (just before billing)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(., 'Delivery address')]")))

    print("✅ Arrived at delivery address step, just before billing.")

    time.sleep(5)  # Pause to visually confirm

finally:
    driver.quit()
