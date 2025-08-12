import requests


base_url = "https://kinopoiskapiunofficial.tech"
key = "55982dd8-58b9-4538-9408-2d1dfd0ff8d8"
headers = {
    "X-API-KEY": key,
    "Content-Type": "application/json"
}


def test_word_russuian_name():
    resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=солнце&page=1", headers=headers)
    assert resp.status_code == 200


def test_word_english_name():
    resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=Star&page=1", headers=headers)
    assert resp.status_code == 200


def test_init_name():
    resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=13&page=1", headers=headers)
    assert resp.status_code == 200


def test_miss_symbol():
    resp = requests.get(base_url + "/api/v2.1/films/search-by-keywordkeyword=Star&page=1", headers=headers)
    assert resp.status_code == 400


def test_no_auth():
    resp = requests.get(base_url + "/api/v2.1/films/search-by-keyword?keyword=Star&page=1")
    assert resp.status_code == 401
