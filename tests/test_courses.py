import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):

    # chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    #
    # courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    # expect(courses_title).to_be_visible()
    # expect(courses_title).to_have_text('Courses')
    #
    # empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    # expect(empty_view_icon).to_be_visible()
    #
    # empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    # expect(empty_view_title).to_be_visible()
    # expect(empty_view_title).to_have_text('There is no results')
    #
    # empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    # expect(empty_view_description).to_be_visible()
    # expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")

    courses_list_page.toolbar_view.check_visible()
    # courses_list_page.check_visible_courses_title()
    # courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()




@pytest.mark.regression
@pytest.mark.courses
def test_create_course(chromium_page_with_state, create_course_page, courses_list_page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    # create_course_page.check_visible_image_preview_empty_view()
    # create_course_page.check_visible_image_upload_view()
    # Остальной код без изменений
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    create_course_page.check_visible_create_course_form(title="", description="", estimated_time="", max_score="0", min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # create_course_page.upload_preview_image("/Users/uladzimirrudnik/PycharmProjects/Python_Playwright/testdata/files/image.jpg")
    # create_course_page.check_visible_image_upload_view()
    # Остальной код без изменений
    create_course_page.image_upload_widget.upload_preview_image('/Users/uladzimirrudnik/PycharmProjects/Python_Playwright/testdata/files/image.jpg')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10")
    create_course_page.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    # courses_list_page.check_visible_courses_title()
    # courses_list_page.check_visible_create_course_button()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )



