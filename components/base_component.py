import allure
from typing import Pattern
from playwright.sync_api import Page, expect
from tools.logger import get_logger




logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    """
    Base class for all UI components.
    
    Provides common functionality and Playwright page context to all derived components.
    """
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """
        Asserts that the current page URL matches the provided regular expression pattern.
        """
        step = f'Checking that the current url is "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
