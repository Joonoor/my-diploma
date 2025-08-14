import allure
import requests
from config import *


@allure.title("Поиск фильма на кириллице")
@allure.description(
    "Проверяет корректность поиска на кириллице")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_word_russuian_name():

    with allure.step("Вход на сайт, ввод в поле запрос на кириллице"):
        resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=Мулан&page=1", headers=headers)

    with allure.step("Проводим проверку"):
        assert resp.status_code == 200
        assert resp.json()["keyword"] == "Мулан"


@allure.title("Поиск фильма на латинице")
@allure.description(
    "Проверяет корректность поиска фильма на латиницей")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_word_english_name():

    with allure.step("Вход на сайт, ввод в поле запрос на латинице"):
        resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=Star&page=1", headers=headers)

    with allure.step("Проводим проверку"):
        assert resp.status_code == 200
        assert resp.json()["keyword"] == "Star"


@allure.title("Поиск фильма по цифрам")
@allure.description(
    "Проверяет корректность поиска фильма по цифрам")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_init_name():

    with allure.step("Вход на сайт, ввод в поле запрос с цифрами в тексте"):
        resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=13&page=1", headers=headers)

    with allure.step("Проводим проверку"):
        assert resp.status_code == 200
        assert resp.json()["films"][0]["nameRu"] == "13 клиническая"


@allure.title("Статус код при неправльном URL")
@allure.description(
    "Ожидается наличие ошибки при неправильном URL")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
def test_miss_symbol():

    with allure.step("Вход на сайт и поиск фильма с пропущенным '?' "):
        resp = requests.get(base_url + "/api/v2.1/films/search-by-keywordkeyword=Star&page=1", headers=headers)

    with allure.step("Проводим проверку"):
        assert resp.status_code == 400


@allure.title("Вход на сайт без авторизации")
@allure.description(
    "Ожидается наличие ошибки при входе без авторизации")
@allure.feature("Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_no_auth():

    with allure.step("Входим на сайт, забывая добавить ключ авторизации"):
        resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=Star&page=1")

    with allure.step("Проводим проверку"):
        assert resp.status_code == 401
        assert "You don't have permissions." in resp.json()["message"]
