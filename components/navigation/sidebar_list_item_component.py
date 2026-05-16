from re import Pattern
import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    """
    Component representing an individual navigation item within the sidebar.
    
    Handles interaction and visibility checks for the item's icon, title, and button.
    """
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'list-item-icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'item-title-text')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'list-item-button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        """
        Asserts that the sidebar list item displays correctly with its icon, title text, and clickable area.
        """
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        """
        Clicks the navigation item and asserts the URL updates to the expected route pattern.
        """
        self.button.click()
        self.check_current_url(expected_url)