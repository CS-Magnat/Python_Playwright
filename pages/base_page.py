from typing import Pattern

import allure
from playwright.sync_api import Page, expect  # Импортируем класс Page

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("BASE_PAGE")  # Инициализируем logger

class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод для открытия ссылок
        step = f'Opening the url "{url}"'
        with allure.step(step):  # Добавили allure.step
            logger.info(step)  # Добавили логирование
            self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        step = f'Reloading the page with url "{self.page.url}"'
        with allure.step(step):  # Добавили allure.step
            logger.info(step)  # Добавили логирование
            self.page.reload(wait_until='domcontentloaded')

    # Метод для проверки текущего URL
    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that the current url is "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)  # Добавили логирование
            # Добавили allure.step
            expect(self.page).to_have_url(expected_url)