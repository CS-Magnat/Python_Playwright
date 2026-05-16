from playwright.sync_api import Page
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent


class CoursesListPage(BasePage):
    """
    Page object representing the main list of courses.
    
    Provides access to the courses grid, toolbar, navigation components, and the empty state view.
    """
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        self.course_view = CourseViewComponent(page)


    def check_visible_empty_view(self):
        """
        Asserts that the empty view component is visible with the expected title and description
        when there are no courses to display.
        """
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

