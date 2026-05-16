import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    """
    Component representing the form used to create or edit a course.
    
    Provides methods to fill out the form fields and verify their visibility and current values.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'course-form-title')
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'course-form-estimated-time')
        self.create_course_description_textarea = Textarea(page, 'create-course-form-description-input', 'course-form-description')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'course-form-max-score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'course-form-min-score')

    @allure.step("Fill create course form")
    def fill(self, title, estimated_time, description, max_score, min_score):
        """
        Populates the course creation form with the provided details.
        Also performs a quick assertion to verify each field was correctly filled.
        
        Args:
            title: The name of the course.
            estimated_time: Expected duration to complete the course.
            description: Detailed description of the course content.
            max_score: Maximum achievable score for the course.
            min_score: Minimum score required to pass.
        """
        self.create_course_title_input.fill(title)
        self.create_course_title_input.check_have_value(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_estimated_time_input.check_have_value(estimated_time)
        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea.check_have_value(description)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input.check_have_value(max_score)
        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input.check_have_value(min_score)

    @allure.step("Check visible create course form")
    def check_visible(self, title, estimated_time, description, max_score, min_score):
        """
        Asserts that all form fields are visible and contain the expected values.
        
        Args:
            title: Expected course name.
            estimated_time: Expected duration.
            description: Expected description text.
            max_score: Expected maximum score.
            min_score: Expected minimum score.
        """
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)
        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(estimated_time)
        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)
        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)
        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)