from re import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    # Принимаем идентификатор компонента, например dashboard
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Формируем локаторы динамически
        # self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        # self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        # self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'list-item-icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'item-title-text')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'list-item-button')

    def check_visible(self, title: str):
        # expect(self.icon).to_be_visible()
        self.icon.check_visible()


        # expect(self.title).to_be_visible()
        # expect(self.title).to_have_text(title)
        self.title.check_visible()
        self.title.check_have_text(title)

        # expect(self.button).to_be_visible()
        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)