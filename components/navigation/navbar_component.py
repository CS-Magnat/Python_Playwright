import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    """
    Component representing the application's top navigation bar.
    
    Responsible for displaying the application title and the user's welcome message.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page,'navigation-navbar-app-title-text', 'App title')
        self.welcome_title = Text(page,'navigation-navbar-welcome-title-text', 'Welcome title')


    @allure.step('Check visible navbar for user "{username}"')
    def check_visible(self, username: str):
        """
        Asserts that the navigation bar is visible and displays the correct 
        application title and the personalized welcome message.
        
        Args:
            username: The username expected to be displayed in the welcome message.
        """
        self.app_title.check_have_text('UI Course')
        self.welcome_title.check_have_text(f'Welcome, {username}!')