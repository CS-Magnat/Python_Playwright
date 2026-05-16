from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement
from tools.logger import get_logger



logger = get_logger("INPUT")


class Input(BaseElement):
    """
    Element wrapper for text input fields.
    
    Provides methods to type text into inputs and verify their current values.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Retrieves the Playwright locator for the input element, specifically 
        targeting the underlying <input> tag.
        """
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        """
        Enters the given string value into the input field.
        """
        step = f'Filling "{self.type_of}" with "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Asserts that the input field's current value exactly matches the expected text.
        """
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)