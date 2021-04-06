"""
execute_script
"""
import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    answer = calc(browser.find_element_by_id("input_value").text)

    input_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(answer)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(5)
    browser.quit()
