from playwright.sync_api import Page, Locator


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, **kwargs) -> Locator: # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        # Возвращаем объект локатора
        return self.page.get_by_test_id(locator)