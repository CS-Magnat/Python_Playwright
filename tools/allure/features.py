from enum import Enum


class AllureFeature(str, Enum):
    """
    Allure Features representing functional modules within an Epic.
    Used to group related test suites by application feature in the Allure report.
    """
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    AUTHENTICATION = "Authentication"