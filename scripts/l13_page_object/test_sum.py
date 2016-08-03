# -*- coding:utf-8 -*-

from pages.index_page import IndexPage


def test_check_sum_function(driver, logger):
    first_arg = 1
    second_arg = 2

    index_page = IndexPage(driver)
    logger.info("输入两个加数 %d 和 %d, 并点击求和按钮" % (first_arg, second_arg))
    index_page.caculate_sum(str(first_arg), str(second_arg))
    logger.info("获取求和结果, 检查结果是否为 %d" % (first_arg + second_arg))
    assert index_page.sum_result_label.text == str(first_arg + second_arg)


def test_check_sum_function_should_fail(driver, logger):
    first_arg = 1
    second_arg = 2

    # find elements
    index_page = IndexPage(driver)
    logger.info("输入两个加数 %d 和 %d, 并点击求和按钮" % (first_arg, second_arg))
    index_page.caculate_sum(str(first_arg), str(second_arg))
    logger.info("获取求和结果, 检查结果是否为 %d" % (first_arg + second_arg))
    index_page.caculate_sum(str(first_arg), str(second_arg))
    assert index_page.sum_result_label.text == str(first_arg + second_arg + 1)