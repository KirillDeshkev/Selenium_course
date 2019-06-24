from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get(link)

button = browser.find_element_by_id("book")
WebDriverWait(browser, 12, 0.1).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
input_value = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(input_value)

submit_button = browser.find_element_by_id("solve")
submit_button.click()
