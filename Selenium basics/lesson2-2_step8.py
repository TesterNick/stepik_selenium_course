"""
sending files
"""
import os
import time

from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    for name in "firstname", "lastname", "email":
        browser.find_element_by_name(name).send_keys(name)
    path = os.path.abspath("test.txt")
    browser.find_element_by_id("file").send_keys(path)

    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(5)
    browser.quit()
