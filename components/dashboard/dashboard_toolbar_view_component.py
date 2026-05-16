import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    """
    Component representing the top toolbar on the dashboard page.
    
    Currently handles the display of the dashboard title.
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = Text(page, 'dashboard-toolbar-title-text',
                                            'toolbar-title')


    @allure.step("Check visible dashboard toolbar")
    def check_visible(self):
        """
        Asserts that the 'Dashboard' title is correctly displayed in the toolbar.
        """
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')
