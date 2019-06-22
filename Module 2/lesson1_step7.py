from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
input_value = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(input_value)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()
button = browser.find_element_by_class_name("btn")
button.click()
