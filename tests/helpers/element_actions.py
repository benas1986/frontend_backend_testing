"""
Provides Chrome driver for element actions
"""

import logging

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains

LOG = logging.getLogger(__name__)


class ElementActions:
    """
    Class for Chrome driver element actions
    """
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def click(self, element):
        """
        Clicks element
        @param element: element object
        """
        self.actions.click(element)
        self.actions.perform()

    @staticmethod
    def input_text(element, text):
        """
        Inserts text into element
        @param element: element object
        @param text: text any
        """
        element.send_keys(text)
