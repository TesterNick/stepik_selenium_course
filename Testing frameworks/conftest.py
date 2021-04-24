"""
Conftest for test_items.py
"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture()
def browser(request):
    prefs = {'intl.accept_languages': request.config.getoption("language")}
    options = Options()
    options.add_experimental_option('prefs',  prefs)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
