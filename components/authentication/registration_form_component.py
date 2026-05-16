from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    """
    Component representing the user registration form.
    
    Provides methods to input new user details and verify the state of form fields.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    @allure.step("Fill registration form")
    def fill(self, email, username, password):
        """
        Fills the registration form with the provided new user details.
        
        Args:
            email: The email address for the new account.
            username: The desired username.
            password: The password for the new account.
        """
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email, username, password):
        """
        Verifies that the registration form fields display the expected values.
        
        Args:
            email: Expected text in the email field.
            username: Expected text in the username field.
            password: Expected text in the password field.
        """
        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)
