import time
import os

def takeScreenshot(driver):
    fileName = str(round(time.time() * 1000)) + ".png"


    # Ensure the directory exists
    # if not os.path.exists(screenshotdirectory):
    #     os.makedirs(screenshotdirectory)

    # destinationfile = screenshotdirectory + fileName
    # Relative path for screenshots directory
    screenshot_directory = os.path.join(os.getcwd(), "screenshots")

    # Ensure the directory exists
    os.makedirs(screenshot_directory, exist_ok=True)

    # Full path to save the screenshot
    destination_file = os.path.join(screenshot_directory, fileName)


    try:
        driver.save_screenshot(destination_file)
        print("Screenshot saved to directory --> :: " + destination_file)
    except NotADirectoryError:
        print("Not a directory issue")
