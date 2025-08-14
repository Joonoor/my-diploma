import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    """
    Фикстура для запуска и закрытия драйвера.
    После запука драйвера открывает сайт проекта.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.kinopoisk.ru/")
    driver.implicitly_wait(50)
    yield driver
    driver.quit()
