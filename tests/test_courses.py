import pytest
from playwright.sync_api import expect


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

