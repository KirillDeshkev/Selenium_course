from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

first_element = browser.find_element_by_id("num1")
first_number = int(first_element.text)
second_element = browser.find_element_by_id("num2")
second_number = int(second_element.text)
input_value = str(first_number + second_number)

dropdown = Select(browser.find_element_by_id("dropdown"))
dropdown.select_by_value(input_value)
button = browser.find_element_by_class_name("btn")
button.click()
