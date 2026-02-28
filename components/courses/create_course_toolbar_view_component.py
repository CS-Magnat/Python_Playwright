from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        # self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')
        self.create_course_title = Text(page,'create-course-toolbar-title-text', "course-toolbar-title")
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', "course-toolbar-create")


    def check_visible(self, is_create_course_disabled: bool = True):
        if is_create_course_disabled:
            # expect(self.create_course_button).to_be_disabled()
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            # expect(self.create_course_button).to_be_enabled()
            self.create_course_button.check_enabled()

        # expect(self.create_course_title).to_be_visible()
        # expect(self.create_course_title).to_have_text('Create course')
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()