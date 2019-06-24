from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

start_button = browser.find_element_by_class_name("btn")
start_button.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
input_value = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(input_value)

submit_button = browser.find_element_by_class_name("btn")
submit_button.click()
