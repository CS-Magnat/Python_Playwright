import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import expect
#будем инициализировать наш драйвер для доступа ко всем страницам и общие методы

class BasePage:

    # это то, что мы будем инициализировать
    def __init__(self, page):
        self.page = page

    def open(self):
        #в алюр отчете будет отображаться Open и урл страницы
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.page.goto(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            expect(self.page).to_have_url(self.PAGE_URL, timeout=10000)

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.page.screenshot(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )