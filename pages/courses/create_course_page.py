from playwright.sync_api import Page
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    """
    Page object representing the course creation and editing interface.
    
    Provides access to form elements, toolbars, image upload widgets, 
    and exercise management components required to create a new course.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

    def check_visible_exercises_empty_view(self):
        """
        Asserts that the empty state is displayed for the exercises list,
        indicating that no exercises have been added to the course yet.
        """
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )