from enum import Enum


class AllureEpic(str, Enum):
    """
    Allure Epics grouping high-level functional areas of the application.
    Used to categorize tests by business domain in the Allure report.
    """
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"