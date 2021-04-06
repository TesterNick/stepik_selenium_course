"""
find_element_by_id
"""
import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    answer = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector("button.btn").click()
finally:
    # Copy pass code before time is up!
    time.sleep(5)
    browser.quit()
