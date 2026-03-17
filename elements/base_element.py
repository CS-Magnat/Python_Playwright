
from playwright.sync_api import Page, Locator, expect
import allure


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "base element"

    # Метод принимает кейворд аргументы (kwargs)
    # def get_locator(self, **kwargs) -> Locator: # объект Locator для взаимодействия с элементом
    #     # Инициализирует объект локатора, подставляя динамические значения в локатор.
    #     locator = self.locator.format(**kwargs)
    #     # Возвращаем объект локатора
    #     return self.page.get_by_test_id(locator)

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавляем аргумент nth со значением по умолчанию 0
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data-testid={locator}" at index "{nth}"'):  # Добавили шаг
            return self.page.get_by_test_id(locator).nth(nth)  # Теперь выбираем элемент по индексу

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):  # Добавили шаг
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

    # def click(self, **kwargs):
    #     # "Лениво" инициализируем локатор
    #     locator = self.get_locator(**kwargs)
    #     # Выполняем нажатие на элемент
    #     locator.click()
    #
    # def check_visible(self, **kwargs):
    #     # Инициализируем локатор "лениво"
    #     locator = self.get_locator(**kwargs)
    #     # Проверяем, что элемент виден на странице
    #     expect(locator).to_be_visible()
    #
    # def check_have_text(self, text: str, **kwargs):
    #     locator = self.get_locator(**kwargs)
    #     expect(locator).to_have_text(text)