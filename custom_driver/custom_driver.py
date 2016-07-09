#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver


class CustomDriver(webdriver.Remote):

    def tap_element_coordinate(self, el):
        """
        Custom method. Tap element by tapping its coordiante
        :param el: Element instance. Should have location and size attribute
        :return:
        """
        location = el.location
        size = el.size

        x = location["x"] + size["width"] / 2
        y = location["y"] + size["height"] / 2

        self.tap([(x, y)])
