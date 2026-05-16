from playwright.sync_api import expect
import allure
from elements.base_element import BaseElement
from tools.logger import get_logger



logger = get_logger("BUTTON")

class Button(BaseElement):
    """
    Element wrapper for UI buttons.
    
    Provides specialized methods to interact with and assert the state of button elements.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Asserts that the button is currently enabled and clickable.
        """
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Asserts that the button is currently disabled.
        """
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()