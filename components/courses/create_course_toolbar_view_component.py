import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    """
    Component representing the main toolbar on the course creation page.
    
    Contains the primary 'Create course' action button and page title.
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page,'create-course-toolbar-title-text', "course-toolbar-title")
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', "course-toolbar-create")

    @allure.step("Check visible create course toolbar")
    def check_visible(self, is_create_course_disabled: bool = True):
        """
        Asserts the visibility of the toolbar title and the state of the 'Create course' button.
        
        Args:
            is_create_course_disabled: If True, asserts the button is disabled. 
                                       If False, asserts the button is enabled.
        """
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    def click_create_course_button(self):
        """Submits the complete course form."""
        self.create_course_button.click()