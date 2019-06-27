from selenium import webdriver
import time
import unittest


class Registration(unittest.TestCase):
    def test_registration1_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[contains(@placeholder, \"имя\")]")
        input1.send_keys("First name")
        input2 = browser.find_element_by_xpath("//input[contains(@placeholder, \"фамилию\")]")
        input2.send_keys("Last name")
        input3 = browser.find_element_by_xpath("//input[contains(@placeholder, \"Email\")]")
        input3.send_keys("1@1.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

    def test_registration2_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[contains(@placeholder, \"имя\")]")
        input1.send_keys("First name")
        input2 = browser.find_element_by_xpath("//input[contains(@placeholder, \"фамилию\")]")
        input2.send_keys("Last name")
        input3 = browser.find_element_by_xpath("//input[contains(@placeholder, \"Email\")]")
        input3.send_keys("1@1.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")


if __name__ == "__main__":
    unittest.main()
