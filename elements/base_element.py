from playwright.sync_api import Page, Locator, expect
import allure
from tools.logger import get_logger



logger = get_logger("BASE_ELEMENT")

class BaseElement:
    """
    Base class for all UI elements (e.g., buttons, inputs, links).
    
    Wraps Playwright's Locator API to provide standardized interaction methods,
    built-in logging, and automatic Allure step generation.
    """
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        """Returns a string representation of the element's type (e.g., 'button', 'input')."""
        return "base element"


    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Retrieves the Playwright Locator associated with this element.
        Formats the locator string with any provided kwargs and selects the 'nth' match.
        """
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        """
        Clicks the element identified by the locator.
        """
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Asserts that the element is currently visible in the DOM.
        """
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Asserts that the element's inner text exactly matches the expected text.
        """
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
