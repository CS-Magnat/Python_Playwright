from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        # self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        # self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'empty-view-icon')
        self.title = Text(page, f'{identifier}-empty-view-title-text','empty-title-text')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'empty-description-text')

    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        # expect(self.icon).to_be_visible()
        self.icon.check_visible()

        # Проверяем видимость заголовка и его текст
        # expect(self.title).to_be_visible()
        # expect(self.title).to_have_text(title)
        self.title.check_visible()
        self.title.check_have_text(title)

        # Проверяем видимость описания и его текст
        # expect(self.description).to_be_visible()
        # expect(self.description).to_have_text(description)
        self.description.check_visible()
        self.description.check_have_text(description)