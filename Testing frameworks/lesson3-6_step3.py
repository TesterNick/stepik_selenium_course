"""
pytest. Parametrized tests
"""
import math
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize("link", links)
def test_correct_message(browser, link):
    browser.get(link)
    WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
    text_area = browser.find_element_by_tag_name("textarea")
    text_area.send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission").click()
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert text == "Correct!"
