"""
Frontend tests
"""

import logging
from datetime import date
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

from front_end.data import (
    WAY_2_AUTOMATION_SITE,
    ALERT_BOX_CSS_SELECTOR,
    INPUT_ALERT_XPATH,
    INPUT_ALERT_IFRAME_SRC,
    INPUT_ALERT_BUTTON,
    MY_NAME,
    TEXT_ELEMENT_ID,
    DATA_PICKER_WIDGET,
    FORMAT_DATA_XPATH,
    FORMAT_DATA_IFRAME_SRC,
    INPUT_FIELD_XPATH,
    CURRENT_DATE_XPATH,
    FORMAT_OPTION_ID,
    FORMAT_OPTION_TEXT,
)
from helpers.element_actions import ElementActions
from helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)


def go_to_iframe_by_src(element_finder, chrome_driver, src_value):
    """
    Goes to iframe which has src with expected value
    """
    LOG.info("Switching to iframe with src=%s ", src_value)
    iframes = element_finder.list_by_xpath("//iframe")
    for iframe in iframes:
        if src_value in iframe.get_attribute("src"):
            chrome_driver.switch_to.frame(iframe)


def test_alert_your_name(
    chrome_driver: Chrome,
    element_finder: FindElement,
    element_actions: ElementActions,
):
    """
    Check if it is possible add your name to the alert pop-up
    """
    LOG.info("Go to the website: %s", WAY_2_AUTOMATION_SITE)
    chrome_driver.get(WAY_2_AUTOMATION_SITE)
    LOG.info(
        "Click on the Alert box from the “Alert” category located on the bottom of the page"
    )
    alert_box = element_finder.by_css_selector(ALERT_BOX_CSS_SELECTOR)
    element_actions.click(alert_box)
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    LOG.info("Navigate to the INPUT ALERT section")
    input_alert = element_finder.by_xpath(INPUT_ALERT_XPATH)
    element_actions.click(input_alert)
    go_to_iframe_by_src(element_finder, chrome_driver, INPUT_ALERT_IFRAME_SRC)
    LOG.info(
        "Click on the button labeled as “Click the button to demonstrate the Input box.”"
    )
    button = element_finder.by_xpath(INPUT_ALERT_BUTTON)
    element_actions.click(button)
    LOG.info("Enter your name in the alert popup")
    alert = chrome_driver.switch_to.alert
    element_actions.input_text(alert, MY_NAME)
    alert.accept()
    LOG.info(
        "Validate the shown message contains your input data (your name) from the previous step"
    )
    p_text = element_finder.by_id(TEXT_ELEMENT_ID)
    LOG.info("My name: %s", MY_NAME)
    LOG.info("Text element info: %s", p_text.text)
    assert MY_NAME in p_text.text


def test_format_date_isoformat(
    chrome_driver: Chrome,
    element_finder: FindElement,
    element_actions: ElementActions,
):
    """
    Check if it is possible to choose current date and format it with isoformat
    """
    LOG.info("Go to the website: %s", WAY_2_AUTOMATION_SITE)
    chrome_driver.get(WAY_2_AUTOMATION_SITE)
    LOG.info("Open the Date picker widget")
    date_picker = element_finder.by_css_selector(DATA_PICKER_WIDGET)
    element_actions.click(date_picker)
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    LOG.info("Navigate to the FORMAT DATE section")
    input_alert = element_finder.by_xpath(FORMAT_DATA_XPATH)
    element_actions.click(input_alert)
    go_to_iframe_by_src(element_finder, chrome_driver, FORMAT_DATA_IFRAME_SRC)
    LOG.info("Select today's date")
    input_field = element_finder.by_xpath(INPUT_FIELD_XPATH)
    element_actions.click(input_field)
    current_day = element_finder.by_xpath(CURRENT_DATE_XPATH)
    element_actions.click(current_day)
    LOG.info("Select the ISO 8601 Format option")
    select = Select(element_finder.by_id(FORMAT_OPTION_ID))
    select.select_by_visible_text(FORMAT_OPTION_TEXT)
    LOG.info("Get current day iso format from your pc")
    today_date = date.today().isoformat()
    LOG.info("Today's day from pc  %s", today_date)
    date_from_element = input_field.get_attribute("value")
    LOG.info("Today's day from the website %s", date_from_element)
    assert today_date == date_from_element
