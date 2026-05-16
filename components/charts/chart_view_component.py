import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    """
    Component representing a single chart widget on the dashboard.
    
    Validates the presence of the chart's title and its graphical rendering.
    """
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart view "{title}"')
    def check_visible(self, title):
        """
        Asserts that the chart and its corresponding title are displayed.
        """
        self.title.check_visible()
        self.title.check_have_text(title)
        self.chart.check_visible()
