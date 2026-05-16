from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement
from tools.logger import get_logger



logger = get_logger("TEXT_AREA")


class Textarea(BaseElement):
    """
    Element wrapper for multi-line text input fields (<textarea>).
    
    Provides methods for filling text and validating its value.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Retrieves the Playwright locator targeting the underlying <textarea> tag.
        """
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        """
        Enters a multi-line string into the textarea.
        """
        step = f'Filling {self.type_of} "{self.name}" with value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Asserts that the current value of the textarea matches the expected string.
        """
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)