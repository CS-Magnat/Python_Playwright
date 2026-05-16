from playwright.sync_api import Page, Route

def mock_static_resources(page: Page):
    """
    Aborts network requests for heavy static resources (images, fonts, media).
    This significantly reduces page load times and stabilizes test execution.
    """
    page.route("**/*.{ico,png,jpg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort())