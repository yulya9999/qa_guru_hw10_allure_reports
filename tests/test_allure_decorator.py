import allure
from selene import browser, by, be


def test_decorator():
    open_browser('')
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    click_issues()
    issue_should_be_visible('#89')


@allure.step('Открытие {url}')
def open_browser(url):
    browser.open(url)


@allure.step('Поиск репозитория {repository}')
def search_repository(repository):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repository).press_enter()


@allure.step('Выбор репозитория {repository}')
def open_repository(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('Переход в issues')
def click_issues():
    browser.element('#issues-tab').click()


@allure.step('Проверка наличия issue с номером {number}')
def issue_should_be_visible(number):
    browser.element(by.partial_text(number)).should(be.visible)
