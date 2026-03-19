from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement


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
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)