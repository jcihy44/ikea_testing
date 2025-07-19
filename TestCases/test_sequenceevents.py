import pytest
from utilities.takescreenshotevents import takeScreenshot
import time
from PageObjects import navigation
from PageObjects import IkeaPLP
from PageObjects import IkeaPDP
from PageObjects import IkeaSideCart
from PageObjects import IkeaCheckoutPage
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
        self.mn = navigation.IkeaTopNav(self.driver)
        self.tn = navigation.IkeaTabNav(self.driver)
        self.cn = navigation.CatagoryNav(self.driver)
        self.ddn = navigation.DropdownNav(self.driver)
        self.rs = navigation.RoomSlider(self.driver)
        self.brm = navigation.BedMatressSlider(self.driver)
        self.mplp = IkeaPLP.MattressPLP(self.driver)
        self.pdp = IkeaPDP.IndividualPDP(self.driver)
        self.sc = IkeaSideCart.SideCart(self.driver)
        self.checkout = IkeaCheckoutPage.IkeaCheckout(self.driver)
        # self.tn = navigation.IkeaTabNav(self.driver)
        self.mn.close_cookie_modal()
        time.sleep(1)
        self.mn.go_shopping()
        time.sleep(1)
        self.mn.nav_to_home_page()
        time.sleep(1)
        self.mn.close_mini_cookie_modal()
        time.sleep(1)
        self.tn.nav_to_rooms()
        time.sleep(1)
        self.rs.nav_to_bedroom()
        time.sleep(1)
        self.brm.nav_to_mattresses()
        self.mplp.select_mattress()
        self.pdp.select_qty(3)
        self.pdp.add_to_bag()
        time.sleep(5)
        self.sc.go_to_shopping_bag()
        time.sleep(5)
        self.checkout.cont_to_checkout()
        time.sleep(5)
        self.checkout.cont_as_guest()
        time.sleep(10)
        self.checkout.input_zip()
        time.sleep(5)
        # self.checkout.pick_up()
        # time.sleep(5)
        self.checkout.CONTINUE_TO_DETAILS()
        time.sleep(5)
        # self.checkout.fillout_address_form()
        # self.driver.execute_script("window.scrollBy(0, 250);")
        # time.sleep(1)
        time.sleep(5)
        # takeScreenshot(self.driver)



