# -*- coding:utf-8 -*-

from pages.index_page import IndexPage


def test_check_sum_function(driver):
    first_arg = 1
    second_arg = 2

    index_page = IndexPage(driver)
    index_page.caculate_sum(str(first_arg), str(second_arg))
    assert index_page.sum_result_label.text == str(first_arg + second_arg)


def test_check_sum_function_should_fail(driver):
    first_arg = 1
    second_arg = 2

    # find elements
    index_page = IndexPage(driver)
    index_page.caculate_sum(str(first_arg), str(second_arg))
    assert index_page.sum_result_label.text == str(first_arg + second_arg + 1)