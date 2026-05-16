import re
import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Component representing the toolbar on the main courses list page.
    
    Provides navigation to the course creation flow.
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'toolbar-title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'toolbar-create-course')

    @allure.step("Check visible courses list toolbar")
    def check_visible(self):
        """
        Asserts that the toolbar title ('Courses') and the 'Create course' button are visible.
        """
        self.title.check_visible()
        self.title.check_have_text('Courses')
        self.create_course_button.check_visible()

    @allure.step("Check click create course button")
    def click_create_course_button(self):
        """
        Clicks the 'Create course' button and asserts the URL changes to the creation route.
        """
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))