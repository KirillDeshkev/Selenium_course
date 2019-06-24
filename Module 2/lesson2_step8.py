from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("//input[@name=\"firstname\"]")
input1.send_keys("Some first name")
input2 = browser.find_element_by_xpath("//input[@name=\"lastname\"]")
input2.send_keys("Some last name")
input3 = browser.find_element_by_xpath("//input[@name=\"email\"]")
input3.send_keys("Some email")
file_input = browser.find_element_by_id("file")
file_input.send_keys(file_path)
button = browser.find_element_by_class_name("btn")
button.click()
