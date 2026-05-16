import allure
from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Page object representing the user registration page.
    
    Provides access to the registration form and related page navigation links.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_link  = Link(page, 'registration-page-login-link', 'Login')

    @allure.step("Click registration button")
    def click_registration_button(self):
        """
        Submits the registration form.
        """
        self.registration_button.click()

    @allure.step("Click login link")
    def click_login_link(self):
        """
        Navigates back to the login page via the provided link.
        """
        self.login_link.click()