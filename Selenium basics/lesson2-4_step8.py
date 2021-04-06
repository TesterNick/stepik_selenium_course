"""
Getting rid of time.sleep using explicit waits instead
"""
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    price = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element_by_id("book").click()

    answer = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("solve").click()

    print(browser.switch_to.alert.text)
finally:
    browser.quit()
