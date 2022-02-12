"""
Backend tests
"""

import logging
import requests

from back_end.data import JSON_PLACEHOLDER_SITE, EXPECTED_TITLE, USER_DATA

LOG = logging.getLogger(__name__)


def test_get_title():
    """
    Check that a post exists with the title "qui est esse"
    """
    response = requests.get(f"{JSON_PLACEHOLDER_SITE}/posts").json()
    LOG.info("ALL POSTS JSON MESSAGES %s", response)
    expected_message_with_title = [x for x in response if x["title"] == EXPECTED_TITLE]
    LOG.info("MESSAGE WITH EXPECTED TITLE: %s", expected_message_with_title)
    assert expected_message_with_title, "Not found expected title"


def test_create_user():
    """
    Add a new user and specify a name, username and email
    """
    response = requests.post(f"{JSON_PLACEHOLDER_SITE}/users", data=USER_DATA).json()
    LOG.info("ADDED USER POST REQUEST RESULTS: %s", response)
    assert response["name"] == "Kakadu"
    assert response["username"] == "Banadu"
    assert response["email"] == "banadu@march.biz"


def test_response_time():
    """
    Test one API endpoint that will fail if the response time passes a given threshold.
    """
    response = requests.get(f"{JSON_PLACEHOLDER_SITE}/posts")
    expected_response_time_sec = 2
    response_time_sec = response.elapsed.total_seconds()
    LOG.info("GET REQUEST RESPONSE TIME %s", response_time_sec)
    assert (
        expected_response_time_sec >= response_time_sec
    ), "You reached expected response time"
