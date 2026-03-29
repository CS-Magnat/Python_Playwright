import allure
import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page, expect, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов
from _pytest.fixtures import SubRequest  # Импортируем класс SubRequest для аннотации

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение, Добавили аргумент request
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создаем контекст для новой сессии браузера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    # Открываем новую страницу и передаем ее в тест, Открываем новую страницу в контексте
    yield browser.new_page()
    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    # Закрываем браузер после выполнения тестов
    browser.close()

    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False) # Запускаем браузер
    context = browser.new_context()
    page = context.new_page()

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    # page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    # email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user.name@gmail.com')

    # username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')
    #
    # password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')
    registration_page.click_registration_button()
    # registration_button = page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False) # Запускаем браузер
    context = browser.new_context(storage_state="browser-state.json")  # Создаем контекст для новой сессии браузера
    # Создаем контекст вместе с сохраненным состоянием бразуера
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    # Открываем новую страницу и передаем ее в тест
    yield context.new_page()
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    # После выполнения теста закрываем браузер
    browser.close()

    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')