"""
class Select
"""
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    answer = str(x + y)

    Select(browser.find_element_by_id("dropdown")).select_by_value(answer)

    browser.find_element_by_css_selector("button.btn").click()
finally:
    # Copy pass code before time is up!
    time.sleep(5)
    browser.quit()
