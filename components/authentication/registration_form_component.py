from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        # self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        # self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    def fill(self, email, username, password):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self, email, username, password):
        # expect(self.email_input).to_be_visible()
        # expect(self.email_input).to_have_value(email)
        self.email_input.check_have_value(email)

        # expect(self.username_input).to_be_visible()
        # expect(self.username_input).to_have_value(username)
        self.username_input.check_have_value(username)

        # expect(self.password_input).to_be_visible()
        # expect(self.password_input).to_have_value(password)
        self.password_input.check_have_value(password)
