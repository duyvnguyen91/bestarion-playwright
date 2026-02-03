"""Base page with common behavior and the base URL."""

from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"


class BasePage:
    """Base class for all page objects. Provides common navigation and URL."""

    def __init__(self, page: Page, path: str = "") -> None:
        self.page = page
        self.path = path
        self.url = f"{BASE_URL}/{path}" if path else BASE_URL

    def goto(self) -> None:
        """Navigate to this page's URL."""
        self.page.goto(self.url)

    def get_title(self) -> str:
        """Return the page title."""
        return self.page.title()
