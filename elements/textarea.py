from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("TEXT_AREA")  # Инициализируем logger


class Textarea(BaseElement):
    # def get_locator(self, **kwargs) -> Locator:
    #     # Получаем локатор textarea
    #     return super().get_locator(**kwargs).locator('textarea').first
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
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавили аргумент nth и передеаем его в get_locator
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill that {self.type_of} "{self.name}" with value "{value}"'
        with allure.step(step):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)