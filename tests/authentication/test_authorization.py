import pytest  # Импортируем библиотеку pytest
import allure # Импортируем библиотеку allure

from pages.authentication.login_page import LoginPage  # Импортируем LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization  # Добавили маркировку authorization
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
class TestAuthorization:
    @pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")])
    @allure.title("User login with wrong email or password")  # Добавляем человекочитаемый заголовок
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        # Заполняем форму авторизации
        #login_page.fill_login_form(email=email, password=password)
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)
        # Нажимаем кнопку "Login"
        login_page.click_login_button()
        # Проверяем наличие сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()




# def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):# Создаем тестовую функцию
#     # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную
#     chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#     email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
#     email_input.fill(email)
#
#     password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
#     password_input.fill(password)
#
#     login_button = chromium_page.get_by_test_id('login-page-login-button')
#     login_button.click()
#
#     wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
#     expect(wrong_email_or_password_alert).to_be_visible()
#     expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    @allure.title("User login with correct email and password")  # Добавили заголовок
    def test_successful_authorization(self, login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        # Переход на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        # Клик по кнопке "Logout"
        dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @allure.title("Navigation from login page to registration page")  # Добавили заголовок
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")