import re
import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    """
    Component representing the application's main sidebar navigation menu.
    
    Provides methods to verify the presence of navigation links and interact with them 
    to route between major application modules (Dashboard, Courses, Logout).
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step("Check visible sidebar")
    def check_visible(self):
        """
        Asserts that all primary navigation items are visible in the sidebar.
        """
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        """
        Clicks the 'Logout' menu item and waits for the application to navigate 
        to the login page.
        """
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        """
        Clicks the 'Courses' menu item and waits for the application to navigate 
        to the courses list view.
        """
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        """
        Clicks the 'Dashboard' menu item and waits for the application to navigate 
        to the main dashboard view.
        """
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))