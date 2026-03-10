import time

import allure
import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    @allure.title("Edit course")  # Добавили заголовок
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.fill(
            title = "Playwright",
            estimated_time = "2 weeks",
            description = "Playwright",
            max_score = "100",
            min_score = "10"
        )
        create_course_page.image_upload_widget.upload_preview_image('/Users/uladzimirrudnik/PycharmProjects/Python_Playwright/testdata/files/image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        
        create_course_page.create_course_form.fill(
            title="Playwright Edited",
            estimated_time="20 weeks",
            description="Playwright Edited",
            max_score="1000",
            min_score="100"
        )
        create_course_page.image_upload_widget.upload_preview_image(
            '/Users/uladzimirrudnik/PycharmProjects/Python_Playwright/testdata/files/image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        
        # Проверяем заполненность полей ДО нажатия кнопки
        create_course_page.create_course_form.check_visible(
            title="Playwright Edited",
            description="Playwright Edited",
            max_score="1000",
            min_score="100",
            estimated_time="20 weeks"
        )
        
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Финальная проверка на странице списка курсов
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright Edited",
            max_score="1000",
            min_score="100",
            estimated_time="20 weeks"
        )

