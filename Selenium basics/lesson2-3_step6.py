"""
Switching to another tab
"""
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector("button.btn").click()
    browser.switch_to.window(browser.window_handles[1])

    answer = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_css_selector("button.btn").click()

    print(browser.switch_to.alert.text)
finally:
    browser.quit()
