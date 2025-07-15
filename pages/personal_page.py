import allure

from base.base_page import BasePage
from playwright.sync_api import expect
from config.links import Links
class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = "//input[@name='firstName']"
    SAVE_BUTTON = "(//button[@type='submit'])[1]"
    SPINNER = "//div[@class='oxd-loading-spinner']"

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            field = self.page.locator(self.FIRST_NAME_FIELD)
            field.click()
            field.press("Meta+A")
            field.press("Backspace")
            field.fill(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.page.locator(self.SAVE_BUTTON).click()

    @allure.step("Changes has been saved successfuly")
    def is_changes_saved(self):
        expect(self.page.locator(self.SPINNER)).to_be_hidden()
        expect(self.page.locator(self.FIRST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.FIRST_NAME_FIELD)).to_have_value(self.name)
