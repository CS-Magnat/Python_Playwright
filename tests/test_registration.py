from playwright.sync_api import sync_playwright, expect, Page
import pytest  # Импортируем библиотеку pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # registration_page.fill_registration_form(username="username", email='user.name@gmail.com', password='password')
    registration_page.registration_form.fill(username="username", email='user.name@gmail.com', password='password')
    registration_page.registration_form.check_visible(username="username", email='user.name@gmail.com', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()









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
