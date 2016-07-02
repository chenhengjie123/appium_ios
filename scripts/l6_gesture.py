# -*- coding:utf-8 -*-
import os
import unittest
import sys
import shutil

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

SCREENSHOT_FOLDER = "screenshots"

class TestAppiumIosL6(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # open TestApp.app on simulator iPhone 4s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6 Plus'
        desired_caps['app'] = PATH(
            '../app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # clear screenshot
        if os.path.exists(SCREENSHOT_FOLDER):
            shutil.rmtree(SCREENSHOT_FOLDER)

        os.mkdir(SCREENSHOT_FOLDER)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.currentResult = None

        # Go to gesture tab
        self.driver.find_element_by_accessibility_id("Gesture").click()

        sys.exc_clear()

    def tearDown(self):

        if sys.exc_info()[0]:  # Returns the info of exception being handled
            current_method_name = self.id().split(".")[-1]
            # take screenshot
            self.driver.save_screenshot(os.path.join(SCREENSHOT_FOLDER, "%s.png" % current_method_name))

        # Back to gesture tab
        self.driver.find_element_by_accessibility_id("Gesture").click()





    def test_driver_swipe(self):
        # go to table view
        self.driver.find_element_by_accessibility_id("TableView(swipe and find in scroll view)").click()

        # swipe
        self.driver.swipe(start_x = 100, start_y = 100, end_x = 200, end_y = 200, duration = 1000)

        element1 = None
        element2 = None
        # drag and drop
        self.driver.drag_and_drop(element1, element2)

        pass





    def test_gesture_lock(self):
        # go to gesture lock view
        self.driver.find_element_by_accessibility_id("Gesture Locker (TouchAction)").click()

        btn1 = self.driver.find_element_by_accessibility_id("Button1")
        btn2 = self.driver.find_element_by_accessibility_id("Button2")

        action = TouchAction(self.driver)

        # move from button 1 to button 2
        action.press(btn1).wait(100).move_to(btn2).wait(100).release().perform()

        pass





    def test_scroll_to_element(self):
        # go to table view
        self.driver.find_element_by_accessibility_id("TableView(swipe and find in scroll view)").click()

        # find element
        z_item = self.driver.find_element_by_accessibility_id("s")

        # scroll to visible
        z_item.click()

        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL6)
    unittest.TextTestRunner(verbosity=2).run(suite)
