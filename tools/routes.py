from enum import Enum

class AppRoute(str, Enum):
    """
    Enumeration of all application frontend routes.
    Used to avoid hardcoded strings when navigating within tests.
    """
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"

