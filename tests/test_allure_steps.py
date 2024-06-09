import allure
from selene import by, browser, be


def test_allure_steps():
    with allure.step('Открытие браузера'):
        browser.open("")

    with allure.step('Поиск репозитория eroshenkoam/allure-example'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(
            'eroshenkoam/allure-example'
        ).submit()

    with allure.step('Выбор репозитория eroshenkoam/allure-example'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переход в issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия issue с номером #89'):
        browser.element(by.partial_text("#89")).should(be.visible)