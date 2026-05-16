from enum import Enum


class AllureStory(str, Enum):
    """
    Allure Stories representing individual user-facing scenarios within a Feature.
    Used to label test methods with their corresponding user story in the Allure report.
    """
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"