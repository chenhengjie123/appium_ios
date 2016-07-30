#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..appium_page_objects import PageObject, page_element

class IndexPage(PageObject):
    first_arg_textfield = page_element(accessibility_id = "IntegerA")
    second_arg_textfield = page_element(accessibility_id = "IntegerB")
    sum_button = page_element(accessibility_id = "ComputeSumButton")
    sum_result_label = page_element(accessibility_id = "Answer")

    def caculate_sum(self, a, b):
        self.first_arg_textfield = a
        self.second_arg_textfield = b
        self.sum_button.click()