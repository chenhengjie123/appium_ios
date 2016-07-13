# -*- coding:utf-8 -*-
import os
import unittest
import time

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestAppiumIosL10(unittest.TestCase):

    def test_web_on_simulator(self):
        # open TestApp.app on simulator iPhone 4s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6 Plus'
        desired_caps['browserName'] = 'safari'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.get("http://baidu.com")
        time.sleep(10)
        self.driver.save_screenshot("web_simulator.png")

        self.driver.quit()

    def test_web_on_real_device(self):
        # 需要先手动完成 safariLauncher 的 build 和启动 ios_webkit_debug_proxy.
        # 详情参考: https://github.com/appium/appium/blob/v1.4.13/docs/cn/writing-running-appium/mobile-web.cn.md
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 6 Plus'
        desired_caps['browserName'] = 'safari'
        desired_caps['udid'] = '0b2fbaaf7fa0e752ea908b3d1287be783bffdb57'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.get("http://baidu.com")
        time.sleep(10)
        self.driver.save_screenshot("web_real_device.png")

        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL10)
    unittest.TextTestRunner(verbosity=2).run(suite)
