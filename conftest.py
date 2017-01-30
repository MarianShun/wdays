import pytest
from selenium import webdriver


@pytest.fixture
def selenium():
    browser = webdriver.Chrome()
    return browser
