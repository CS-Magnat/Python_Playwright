"""
Page Object fixtures for the test suite.
Each fixture provides a fully initialized Page Object Model instance
backed by the appropriate browser page (unauthenticated or pre-authenticated).
"""

import pytest
from playwright.sync_api import Page
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    """Provides a LoginPage instance initialized with a fresh browser page."""
    return LoginPage(page=chromium_page)

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """Provides a RegistrationPage instance initialized with a fresh browser page."""
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """Provides an unauthenticated DashboardPage instance."""
    return DashboardPage(page=chromium_page)

@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    """Provides a CoursesListPage instance using a pre-authenticated browser session."""
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    """Provides a CreateCoursePage instance using a pre-authenticated browser session."""
    return CreateCoursePage(page=chromium_page_with_state)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    """Provides an authenticated DashboardPage instance, bypassing the login step."""
    return DashboardPage(page=chromium_page_with_state)