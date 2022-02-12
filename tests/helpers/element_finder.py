"""
Provides Chrome driver
"""

import logging
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

LOG = logging.getLogger(__name__)


class FindElement:
    """
    Class for finding elements with Chrome driver
    """
    def __init__(self, driver: Chrome):
        self.driver = driver

    def by_css_selector(self, locator: str):
        """
        Finds element by css selector
        Explicitly waits element for 30 seconds
        """
        element = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        LOG.debug("element_by_css_celector %s", element)
        return element

    def by_id(self, locator: str):
        """
        Finds element by id
        Explicitly waits element for 30 seconds
        """
        element = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.ID, locator)))
        LOG.debug("element_by_id %s", element)
        return element

    def by_class_name(self, locator: str):
        """
        Finds element by class name
        Explicitly waits element for 30 seconds
        """
        element = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.CLASS_NAME, locator)))
        LOG.debug("element_by_class_name %s", element)
        return element

    def by_xpath(self, locator: str):
        """
        Finds element by xpath
        Explicitly waits element for 30 seconds
        """
        element = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, locator)))
        LOG.debug("element_by_xpath %s", element)
        return element

    def list_by_tag_name(self, locator: str):
        """
        Finds element list by tag name
        """
        elements = self.driver.find_elements(By.TAG_NAME, locator)
        LOG.debug("elements_by_tag %s", elements)
        return elements

    def list_by_xpath(self, locator: str):
        """
        Finds element list by xpath
        """
        elements = self.driver.find_elements(By.XPATH, locator)
        LOG.debug("elements_by_xpath %s", elements)
        return elements

    def list_by_class_name(self, locator: str):
        """
        Finds element list by class name
        """
        elements = self.driver.find_elements(By.CLASS_NAME, locator)
        LOG.debug("elements_by_class_name %s", elements)
        return elements

    def list_by_css_selector(self, locator: str):
        """
        Finds element list by css selector
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
        LOG.debug("elements_by_css_selector %s", elements)
        return elements
