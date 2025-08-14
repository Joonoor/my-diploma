import allure
from selenium.webdriver.common.by import By


@allure.title("Поиск фильма на кириллице")
@allure.description(
    "Проверяет корректность поиска на кириллице")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_russian_word(driver):

    with allure.step("Ищем поисковую строку и вводим в поле нужный тект"):
        driver.find_element(By.NAME, "kp_query").send_keys("Марвел")

    with allure.step("Проводим проверку"):
        assert driver.find_element(By.ID, "suggest-item-film-843859")


@allure.title("Поиск фильма на латинице")
@allure.description(
    "Проверяет корректность поиска фильма на латиницей")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_english_word(driver):

    with allure.step("Ищем поисковую строку и вводим в поле нужный тект"):
        driver.find_element(By.NAME, "kp_query").send_keys("marvel")

    with allure.step("Проводим проверку"):
        assert driver.find_element(By.ID, "suggest-item-film-843859")


@allure.title("Поиск фильма по цифрам")
@allure.description(
    "Проверяет корректность поиска фильма по цифрам")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_init(driver):

    with allure.step("Ищем поисковую строку и вводим в поле нужный тект"):
        driver.find_element(By.NAME, "kp_query").send_keys("13")

    with allure.step("Проводим проверку"):
        assert driver.find_element(By.ID, "suggest-item-tvSeries-4902970")


@allure.title("Поиск фильма символами")
@allure.description(
    "Проверяет способность найти фильм по символам")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
def test_symbol(driver):

    with allure.step("Ищем поисковую строку и вводим в поле нужный тект"):
        driver.find_element(By.NAME, "kp_query").send_keys("%#@#&")

    with allure.step("Проводим проверку"):
        assert driver.find_element(
            By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


@allure.title("Видимость страницы после поиска")
@allure.description(
    "Проверка отображения страницы фильма после перехода из строки поиска")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_tittle(driver):

    with allure.step("Ищем поисковую строку и вводим в поле нужный тект"):
        driver.find_element(By.NAME, "kp_query").send_keys("Марвел")

    with allure.step("Переходим в карточку фильма"):
        driver.find_element(By.ID, "suggest-item-film-843859").click()

    with allure.step("Проводим проверку"):
        assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Капитан Марвел (2019)"
