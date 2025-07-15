import allure

from base.base_page import BasePage
from config.links import Links

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    SUBMIT_FIELD = "//button[@type='submit']"

    @allure.step("Enter login")
    def enter_login(self, login):
        self.page.locator(self.USERNAME_FIELD).fill(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.page.locator(self.PASSWORD_FIELD).fill(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.page.locator(self.SUBMIT_FIELD).click()

