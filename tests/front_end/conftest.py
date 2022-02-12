"""
Configuration for frontend tests
"""

import logging
from webbrowser import Chrome

from pytest import fixture

from helpers.chrome_browser import ChromeDriver
from helpers.element_actions import ElementActions
from helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)


@fixture(scope="function")
def chrome_driver():
    """
    Setup and teardown Chrome driver for each test
    """
    driver = ChromeDriver()
    yield driver.start()
    driver.stop()


@fixture(scope="function")
def element_finder(chrome_driver: Chrome):  # pylint: disable=redefined-outer-name
    """
    :return Chrome driver element finder
    """
    return FindElement(chrome_driver)


@fixture(scope="function")
def element_actions(chrome_driver: Chrome):  # pylint: disable=redefined-outer-name
    """
    :return Chrome driver element actions
    """
    return ElementActions(chrome_driver)
