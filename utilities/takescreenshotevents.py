import time
import os

def takeScreenshot(driver):
    fileName = str(round(time.time() * 1000)) + ".png"
    screenshotdirectory = "C:\\Users\\jcihy\\PycharmProjects\\google_hotel_prices\\screenshots\\"

    # Ensure the directory exists
    # if not os.path.exists(screenshotdirectory):
    #     os.makedirs(screenshotdirectory)

    destinationfile = screenshotdirectory + fileName

    try:
        driver.save_screenshot(destinationfile)
        print("Screenshot saved to directory --> :: " + destinationfile)
    except NotADirectoryError:
        print("Not a directory issue")
