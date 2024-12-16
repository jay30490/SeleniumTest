import allure
import pytest
from selenium import webdriver
import time

link = 'https://demoqa.com/login'


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # COMMENT THE FOLLOWING LINE TO DISABLE HEADLESS CHROME MODE
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--verbose')
    options.page_load_strategy = 'none'
    browser = webdriver.Chrome(options = options)

    try:
        browser.get(link)
        browser.implicitly_wait(10)
        yield browser
    finally:
        time.sleep(2)
        browser.quit()
