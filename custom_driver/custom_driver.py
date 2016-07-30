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

    def zoom(self, element=None, percent=200, steps=50):
        # calculate startX, startY, endX, endY our self
        location = element.location
        size = element.size

        startX = location["x"] + size["width"] / 2
        startY = location["x"] + size["height"] / 2

        # calculate end location using percentage
        endX = startX + size["width"] / 2 * (percent - 100) / 100.0
        endY = startY + size["height"] / 2 * (percent -100) / 100.0

        opts = {
            'startX': startX,
            'startY': startY,
            'endX': endX,
            'endY': endY,
            'duration': steps / 10
        }
        self.execute_script('mobile: pinchOpen', opts)
        return self