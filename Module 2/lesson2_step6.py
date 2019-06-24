from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
input_value = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(input_value)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()
button = browser.find_element_by_class_name("btn")
button.click()
