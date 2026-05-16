from typing import Pattern
import allure
from playwright.sync_api import Page, expect
from tools.logger import get_logger



logger = get_logger("BASE_PAGE")

class BasePage:
    """
    Base class for all Page Object Models (POMs).
    
    Provides common navigation and verification methods shared across all pages.
    """
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        """
        Navigates to the specified URL and waits until the network is idle.
        """
        step = f'Opening the url "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """
        Reloads the current page and waits until the DOM content is fully loaded.
        """
        step = f'Reloading the page with url "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        """
        Asserts that the current page URL matches the provided regular expression pattern.
        """
        step = f'Checking that the current url is "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)