import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", autouse=True)
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--window-size=1920,1080"
            ]
        )
        page = browser.new_page()
        yield page
        browser.close()
