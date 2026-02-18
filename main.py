import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_google_web(driver):
    url = "https://www.google.com/?hl=RU"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url
