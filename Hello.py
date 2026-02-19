# Домашняя задание хранится на платформе
# Шаблог для автотеста из пункта 3 и 4
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver: WebDriver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


# Код который нужно исправить для пункта 5

print("Hello, README!")
text = (
    "Lorem Ipsum - это текст-'рыба', часто используемый в печати и вэб-дизайне. "
    "Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века."
    " В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, "
    "используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил "
    "без заметных изменений пять веков, но и перешагнул в электронный дизайн. "
    "Его популяризации в новое время послужили публикация листов Letraset с образцами"
    "Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа"
    " Aldus PageMaker, в шаблонах которых используется Lorem Ipsum."
)


def add(a, b):
    return a + b


def greet(name):
    print("Привет," + name)


numbers = [1, 2, 3, 4, 5]
greet("мир")
print(add(2, 2))
