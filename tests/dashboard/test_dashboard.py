import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD) # Добавили теги
class TestDashboard:
    @allure.title("Check displaying of dashboard page")  # Добавили заголовок
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.sidebar.check_visible()
        # Добавили проверку Navbar компонента на странице Dashboard
        dashboard_page_with_state.navbar.check_visible("username")

        # dashboard_page_with_state.check_visible_dashboard_title()
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        # dashboard_page_with_state.check_visible_scores_chart()
        # dashboard_page_with_state.check_visible_courses_chart()
        # dashboard_page_with_state.check_visible_students_chart()
        # dashboard_page_with_state.check_visible_activities_chart()
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')