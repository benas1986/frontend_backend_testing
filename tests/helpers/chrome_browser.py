"""
Provides Chrome driver
"""

import logging

from selenium import webdriver

LOG = logging.getLogger(__name__)


class ChromeDriver:
    """
    Class for starting and stopping Chrome driver
    """
    def __init__(self):
        self.driver = None

    def start(self):
        """
        Starts Chrome driver
        """
        LOG.debug("CONNECTING TO CHROME DRIVER")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)  # seconds
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1920, 1080)
        return self.driver

    def stop(self):
        """
        Stops Chrome driver
        """
        LOG.debug("CLOSING CHROME DRIVER")
        return self.driver.quit()
