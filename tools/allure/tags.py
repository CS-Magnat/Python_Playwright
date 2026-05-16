from enum import Enum


class AllureTag(str, Enum):
    """
    Allure Tags used for filtering and searching tests in the Allure report.
    Tags represent cross-cutting concerns like regression, login flow, or navigation.
    """
    COURSES = "COURSES"
    DASHBOARD = "DASHBOARD"
    REGRESSION = "REGRESSION"
    USER_LOGIN = "USER_LOGIN"
    NAVIGATION = "NAVIGATION"
    REGISTRATION = "REGISTRATION"
    AUTHORIZATION = "AUTHORIZATION"