import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashbosradPage
from pages.personal_page import PersonalPage


class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: DashbosradPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page
        request.cls.data = Data()

        request.cls.login_page = LoginPage(page)
        request.cls.dashboard_page = DashbosradPage(page)
        request.cls.personal_page = PersonalPage(page)
