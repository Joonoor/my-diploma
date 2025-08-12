from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(50)
    yield driver
    driver.quit()


def test_search_russian_word(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Марвел")
    assert driver.find_element(By.ID, "suggest-item-film-843859")


def test_search_english_word(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("marvel")
    assert driver.find_element(By.ID, "suggest-item-film-843859")


def test_search_init(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("13")
    assert driver.find_element(By.ID, "suggest-item-tvSeries-4902970")


def test_symbol(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("%#@#&")
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


def test_tittle(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Марвел")
    driver.find_element(By.ID, "suggest-item-film-843859").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Капитан Марвел (2019)"
