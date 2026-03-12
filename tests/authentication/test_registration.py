import pytest  # Импортируем библиотеку pytest
import allure

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)  # Добавили теги
class TestRegistration:
    @allure.title("Registration with correct email, username and password")  # Добавили заголовок
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # registration_page.fill_registration_form(username="username", email='user.name@gmail.com', password='password')
        registration_page.registration_form.fill(username="username", email='user.name@gmail.com', password='password')
        registration_page.registration_form.check_visible(username="username", email='user.name@gmail.com', password='password')
        registration_page.click_registration_button()
        # dashboard_page.check_visible_dashboard_title()
        dashboard_page.dashboard_toolbar_view.check_visible()









# def test_successful_registration(chromium_page: Page):  # Теперь используем фикстуру
#     chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#
#     email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('user.name@gmail.com')
#
#     username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
#     username_input.fill('username')
#
#     password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
#     password_input.fill('password')
#
#     registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
#     registration_button.click()
#
#     dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
#     expect(dashboard_title).to_be_visible()





    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='browser-state.json')
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    #
    #     page.wait_for_timeout(5000)
