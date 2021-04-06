"""
unittest
"""
import time
import unittest

from selenium import webdriver


class RegistrationTests(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def fill_in_form(self):
        bro = self.browser
        first_name = bro.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("first_name")

        last_name = bro.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("last_name")

        email = bro.find_element_by_css_selector(".first_block .third")
        email.send_keys("email")

        button = bro.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

    def test_registration(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.fill_in_form()
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, "Unexpected text")

    def test_registration_on_the_broken_page(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.fill_in_form()
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, "Unexpected text")


if __name__ == "__main__":
    unittest.main()
