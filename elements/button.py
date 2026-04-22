from playwright.sync_api import expect
import allure
from elements.base_element import BaseElement

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("BUTTON")  # Инициализируем logger


class Button(BaseElement):
    # def check_enabled(self, **kwargs):
    #     locator = self.get_locator(**kwargs)
    #     expect(locator).to_be_enabled()
    #
    # def check_disabled(self, **kwargs):
    #     locator = self.get_locator(**kwargs)
    #     expect(locator).to_be_disabled()

    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "button"


    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_be_disabled()