# -*- coding:utf-8 -*-
import os
import unittest
import time

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestAppiumIosL11(unittest.TestCase):

    def test_hybrid_on_simulator(self):
        # open TestApp.app on simulator iPhone 4s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6 Plus'
        desired_caps['app'] = PATH(
            '../app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 进入 WebView 界面
        self.driver.find_element_by_accessibility_id("WebView").click()
        time.sleep(5)

        # 检查有没有 WebView Context
        if len(self.driver.contexts) == 1:
            raise AssertionError("Cannot find webview")

        # 切换到 WebView Context
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)

        print "WebView: \n%s" % self.driver.page_source

        # 切换回 Native Context
        self.driver.switch_to.context(self.driver.contexts[0])
        print "Native: \n%s" % self.driver.page_source

        self.driver.quit()

    def test_web_on_real_device(self):
        # 需要先手动启动 ios_webkit_debug_proxy.
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['udid'] = '0b2fbaaf7fa0e752ea908b3d1287be783bffdb57'
        desired_caps['app'] = PATH(
            '../app/AppForUITest/appForUITest/build/Debug-iphoneos/appForUITest.ipa'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 进入 WebView 界面
        self.driver.find_element_by_accessibility_id("WebView").click()
        time.sleep(5)

        # 检查有没有 WebView Context
        if len(self.driver.contexts) == 1:
            raise AssertionError("Cannot find webview")

        # 切换到 WebView Context
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)

        print "WebView: \n%s" % self.driver.page_source
        self.driver.save_screenshot("hybrid_webview_real_device.png")

        # 切换回 Native Context
        self.driver.switch_to.context(self.driver.contexts[0])
        print "Native: \n%s" % self.driver.page_source
        self.driver.save_screenshot("hybrid_native_real_device.png")

        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL11)
    unittest.TextTestRunner(verbosity=2).run(suite)
