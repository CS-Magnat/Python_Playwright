import allure
from typing import Pattern

from playwright.sync_api import Page, expect

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("BASE_COMPONENT")  # Инициализируем logger


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    #@allure.step("Check current URL")
    # def check_current_url(self, expected_url: Pattern[str]):
    #     step = f'Checking that the current url is "{expected_url.pattern}"'
    #     logger.info(step)  # Добавили логирование
    #     expect(self.page).to_have_url(expected_url)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that the current url is "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
