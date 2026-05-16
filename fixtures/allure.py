import pytest
from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    """
    Session-scoped fixture that automatically generates the Allure environment file 
    after all tests have completed. This populates the 'Environment' tab in the report.
    """
    yield
    create_allure_environment_file()