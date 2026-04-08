import allure
import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page, expect, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов
from _pytest.fixtures import SubRequest  # Импортируем класс SubRequest для аннотации

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from config import settings  # Импортируем настройки


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение, Добавили аргумент request
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

    # # Запускаем браузер
    # browser = playwright.chromium.launch(headless=False)
    # # Указываем директорию для сохранения видеозаписей
    # context = browser.new_context(record_video_dir='./videos') # Создаем контекст для новой сессии браузера
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    # # Открываем новую страницу и передаем ее в тест, Открываем новую страницу в контексте
    # # Перенесли инициализацию страницы в отдельную переменную
    # page = context.new_page()
    # #yield browser.new_page()
    # yield page
    # # В данном случае request.node.name содержит название текущего автотеста
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    # # Закрываем браузер после выполнения тестов
    # browser.close()
    #
    # # Прикрепляем файл с трейсингом к Allure отчету
    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # # Прикрепляем видео автотеста к Allure отчету
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # browser = playwright.chromium.launch(headless=False) # Запускаем браузер
    browser = playwright.chromium.launch(headless=settings.headless)  # Используем settings.headless
    context = browser.new_context()
    page = context.new_page()

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    # page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_form.fill(
        email=settings.test_user.email,  # Используем settings.test_user.email
        username=settings.test_user.username,  # Используем settings.test_user.username
        password=settings.test_user.password  # Используем settings.test_user.password
    )
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

    # context.storage_state(path="browser-state.json")
    context.storage_state(path=settings.browser_state_file)  # Используем settings.browser_state_file
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    # yield from initialize_playwright_page(
    #     playwright,
    #     test_name=request.node.name,
    #     storage_state="browser-state.json"
    # )
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file  # Используем settings.browser_state_file
    )

    #
    #
    # browser = playwright.chromium.launch(headless=False) # Запускаем браузер
    # # Создаем контекст вместе с сохраненным состоянием бразуера
    # # Указываем директорию для сохранения видеозаписей
    # context = browser.new_context(storage_state="browser-state.json", record_video_dir='./videos') # Создаем контекст для новой сессии браузера
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    # # Перенесли инициализацию страницы в отдельную переменную
    # page = context.new_page()
    # # Открываем новую страницу и передаем ее в тест
    # # yield browser.new_page()
    # yield page
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    # # После выполнения теста закрываем браузер
    # browser.close()
    #
    # # Прикрепляем файл с трейсингом к Allure отчету
    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # # Прикрепляем видео автотеста к Allure отчету
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)