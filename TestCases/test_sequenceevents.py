import pytest
from utilities.takescreenshotevents import takeScreenshot
import time
from PageObjects.navigation import Navigation

# class CalendarScreenshot:

# py.test -s -v TestCases/test_sequenceevents.py --browser chrome
# class Testnav:


# def test(setup):
#     # expanding the screen and scrolling
#     driver = setup
#     # self.mn = IkeaMainNav(self.driver)
#     time.sleep(3)
#     driver.execute_script("window.scrollBy(0, 250);")
#     time.sleep(1)
#     takeScreenshot(driver)
#     driver.execute_script("window.scrollBy(0, 400);")
#     time.sleep(1)
#     takeScreenshot(driver)

class Testnav:

    def test_nav(self, setup):
        self.driver = setup
        self.mn = Navigation(self.driver)
        # self.tn = navigation.IkeaTabNav(self.driver)
        self.mn.close_cookie_modal()
        time.sleep(3)
        self.mn.go_shopping()
        time.sleep(2)
        self.mn.nav_to_home_page()
        time.sleep(5)
        # self.driver.execute_script("window.scrollBy(0, 250);")
        # time.sleep(1)
        takeScreenshot(self.driver)



