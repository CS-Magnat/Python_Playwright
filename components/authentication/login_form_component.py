from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    """
    Component representing the user login form.
    
    Handles interactions with the email and password input fields.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    @allure.step("Fill login form")
    def fill(self, email, password):
        """
        Fills the login form with the provided credentials.
        
        Args:
            email: The user's registered email address.
            password: The password associated with the email.
        """
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step("Check visible login form")
    def check_visible(self, email, password):
        """
        Verifies that the form inputs are visible and contain the expected values.
        
        Args:
            email: Expected text in the email field.
            password: Expected text in the password field.
        """
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)