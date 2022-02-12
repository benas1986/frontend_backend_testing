"""
Backend tests
"""

import logging
import requests
import json

from back_end.data import JSON_PLACEHOLDER_SITE, EXPECTED_TITLE, USER_DATA

LOG = logging.getLogger(__name__)


def format_json(response_json):
    """
    Format json for pretty logging
    """
    return json.dumps(response_json, indent=4, sort_keys=True)


def test_get_title():
    """
    Check that a post exists with the title "qui est esse"
    """
    response = requests.get(f"{JSON_PLACEHOLDER_SITE}/posts").json()
    LOG.debug("All posts json messages\n %s", format_json(response))
    LOG.info("Expected title: %s", EXPECTED_TITLE)
    expected_message_with_title = [x for x in response if x["title"] == EXPECTED_TITLE]
    LOG.info("Message with expected title: \n%s", format_json(expected_message_with_title))
    assert expected_message_with_title, "Not found expected title"


def test_create_user():
    """
    Add a new user and specify a name, username and email
    """
    response = requests.post(f"{JSON_PLACEHOLDER_SITE}/users", data=USER_DATA).json()
    LOG.info("User data \n%s", format_json(USER_DATA))
    LOG.info("Added user post request results: \n%s", format_json(response))
    assert response["name"] == "Kakadu"
    assert response["username"] == "Banadu"
    assert response["email"] == "banadu@march.biz"


def test_response_time():
    """
    Test one API endpoint that will fail if the response time passes a given threshold.
    """
    response = requests.get(f"{JSON_PLACEHOLDER_SITE}/posts")
    expected_response_time_sec = 2
    LOG.info("Expected response time sec %s", expected_response_time_sec)
    response_time_sec = response.elapsed.total_seconds()
    LOG.info("Get request response time sec %s", response_time_sec)
    assert (
        expected_response_time_sec >= response_time_sec
    ), "You reached expected response time!!!"
