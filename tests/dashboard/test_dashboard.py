import allure
import pytest
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestDashboard:
    """
    Test suite for verifying the Dashboard page layout and components.
    """

    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        """
        Verifies that all main components of the dashboard page are rendered correctly 
        for an authenticated user.
        """
        # Arrange: Navigate to the dashboard page using a pre-authenticated session state
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        
        # Act & Assert: Check visibility of the navigation components
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        
        # Assert: Check visibility of all statistical charts on the dashboard
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')