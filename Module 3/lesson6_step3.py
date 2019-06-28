import pytest
from selenium import webdriver
import math
import time

expected_message = "Correct!"


def get_answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson_number',
                         ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestAlienMessages(object):
    def test_success_message_is_correct(self, browser, lesson_number):
        link = "https://stepik.org/lesson/{}/step/1".format(lesson_number)
        browser.get(link)
        input_field = browser.find_element_by_tag_name("textarea")
        input_field.send_keys(get_answer())
        send_button = browser.find_element_by_class_name("submit-submission")
        send_button.click()
        success_message_element = browser.find_element_by_tag_name("pre")
        success_message = success_message_element.text
        assert success_message == expected_message, "Expected to find '{}', but found '{}'".format(expected_message,
                                                                                                   success_message)
