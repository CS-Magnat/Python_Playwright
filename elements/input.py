from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("INPUT")  # Инициализируем logger


class Input(BaseElement):
    # def get_locator(self, **kwargs) -> Locator:
    #     return super().get_locator(**kwargs).locator('input')
    #
    # def fill(self, value: str, **kwargs):
    #     locator = self.get_locator(**kwargs)
    #     locator.fill(value)
    #
    # def check_have_value(self, value: str, **kwargs):
    #     locator = self.get_locator(**kwargs)
    #     expect(locator).to_have_value(value)

    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавили аргумент nth и передеаем его в get_locator
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            step = f'Fill with "data-testid={locator}" at index "{nth}"'
            logger.info(step)  # Добавили логирование
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_have_value(value)