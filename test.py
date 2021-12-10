import pytest
import allure
from selenium.webdriver.common.keys import Keys


@allure.suite("language")
@allure.story("test for language checking/switching")
def test_language_change(browser):
    with allure.step("language UA check"):
        pytest.page.getLang("uk").click()
        menu = pytest.page.getMenuElements()
        print(menu)
        assert "вхід" in menu

    with allure.step("language RU switch"):
        pytest.page.getLang("ru").click()
        menu = pytest.page.getMenuElements()
        print(menu)
        assert "вход" in menu


@allure.suite("search by product name")
@allure.story("test for searching")
def test_search_rez_page(browser):
    search_term = "samsung"
    with allure.step("find " + search_term):
        pytest.page.getSearchBox().send_keys(search_term)
        pytest.page.getSearchBox().send_keys(Keys.RETURN)

    with allure.step("headline check"):
        actual_text = pytest.page.getHeadline()
        expected_text = search_term
        assert actual_text == expected_text
