# -*- coding:utf-8 -*-
import os
import unittest
import sys
import shutil

from custom_driver.custom_driver import CustomDriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestAppiumIosL9(unittest.TestCase):

    def setUp(self):
        # open TestApp.app on simulator iPhone 4s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6 Plus'
        desired_caps['app'] = PATH(
            '../app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )

        self.driver = CustomDriver('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        pass

    def test_custom_tap(self):
        el = self.driver.find_element_by_accessibility_id("Gesture")
        self.driver.tap_element_coordinate(el)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL9)
    unittest.TextTestRunner(verbosity=2).run(suite)
