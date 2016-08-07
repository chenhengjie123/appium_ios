#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import os

from appium import webdriver
import pytest


PY3 = sys.version_info[0] == 3
framework_dir = os.path.join(os.path.abspath(__file__), "..")

logging.basicConfig(level = logging.INFO,
                    filename = os.path.join(framework_dir, "test.log"),
                    filemode = "w",
                    stream = sys.stdout,
                    format = "%(asctime)s - [%(name)s] %(levelname)s: %(message)s")
framework_logger = logging.getLogger("pytest")

@pytest.mark.trylast
def pytest_runtest_setup(item):
    framework_logger.info("==Begin to run test case %s==" % item.name)


@pytest.fixture(scope = 'function')
def logger(request):
    # set function name as tag automatically
    test_logger = logging.getLogger(request.function.func_name)

    return test_logger


def pytest_addoption(parser):
    parser.addoption("--app_path", help="path of app file. Should be related path of l13_page_object folder", required=True)
    parser.addoption("--platform", help = "platform of device", required = True)
    parser.addoption("--device_name", help = "name of device", required = True)
    parser.addoption("--device_udid", help = "udid of device")


@pytest.fixture(scope = 'session')
def app_path(request):
    option_app_path = request.config.getoption('app_path')
    app_path = os.path.join(framework_dir, option_app_path)
    return app_path


@pytest.fixture(scope = 'session')
def device_name(request):
    return request.config.getoption('device_name')


@pytest.fixture(scope = 'session')
def platform(request):
    return request.config.getoption('platform')


@pytest.fixture(scope = 'session')
def device_udid(request):
    return request.config.getoption('device_udid')


@pytest.fixture(scope = 'session')
def driver(request, app_path, platform, device_name, device_udid):
    # equals to setUp
    desired_caps = {}
    desired_caps['platformName'] = platform
    desired_caps['deviceName'] = device_name
    desired_caps['udid'] = device_udid
    desired_caps['app'] = app_path

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.node._driver = driver
    # equals to tearDown
    request.addfinalizer(driver.quit)

    return driver

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    summary = []
    extra = getattr(report, 'extra', [])
    driver = getattr(item.session, '_driver', None)
    failure = report.failed



    # add log
    if report.when == "setup":
        framework_logger.info("==Finish running setup of test case %s" % item.name)
        framework_logger.info("**Test result of setup: %s" % report.outcome)
    if report.when == "call":
        # only log result of test case itself. Skip setup and teardown
        framework_logger.info("==Finish running test case %s" % item.name)
        framework_logger.info("**Test result of test case: %s**" % report.outcome)
    if report.when == "teardown":
        framework_logger.info("==Finish running teardown of %s" % item.name)
        framework_logger.info("**Test result of teardown: %s" % report.outcome)

    if not report.passed:
        framework_logger.info("%s infos: %s" % (report.outcome.capitalize(), str(report.longrepr.reprcrash)))
        framework_logger.error("%s traceback: %s" % (report.outcome.capitalize(), str(report.longrepr.reprtraceback)))



    if driver is not None:
        if failure:
            _gather_screenshot(item, report, driver, summary, extra)
            _gather_page_source(item, report, driver, summary, extra)

    if summary:
        report.sections.append(('pytest-appium', '\n'.join(summary)))
    report.extra = extra


def _gather_screenshot(item, report, driver, summary, extra):
    try:
        screenshot = driver.get_screenshot_as_base64()
    except Exception as e:
        summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add screenshot to the html report
        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))


def _gather_page_source(item, report, driver, summary, extra):
    try:
        html = driver.page_source
        if not PY3:
            html = html.encode('utf-8')
    except Exception as e:
        summary.append('WARNING: Failed to gather Page Source: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add page source to the html report
        extra.append(pytest_html.extras.text(html, 'HTML'))