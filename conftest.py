"""
Root pytest configuration file.
Registers all fixture modules so they are auto-discovered by pytest across the entire test suite.
"""

pytest_plugins = (
    "fixtures.pages",
    "fixtures.allure",
    "fixtures.browsers"
)