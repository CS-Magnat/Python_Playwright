import pytest
from playwright.sync_api import expect
from pages.create_course_page import CreateCoursePage

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):

    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar).not_to_be_disabled()
    expect(courses_toolbar).to_have_text("Courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title).not_to_be_disabled()
    expect(courses_title).to_have_text("There is no results")

    chromium_page_with_state.wait_for_timeout(5000)



@pytest.mark.regression
@pytest.mark.courses
def test_create_course(chromium_page_with_state, create_course_page, courses_list_page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(title="", description="", estimated_time="", max_score="0", min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("/Users/uladzimirrudnik/PycharmProjects/Python_Playwright/testdata/files/image.jpg")
    create_course_page.check_visible_image_upload_view()

    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10")
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title = "Playwright",
        estimated_time = "2 weeks",
        max_score = "100",
        min_score = "10")

    chromium_page_with_state.wait_for_timeout(5000)


