"""Login page for Saucedemo. Uses data-testid selectors for stability."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Saucedemo login page: username, password, login button."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, "")

    # Selectors: Saucedemo uses data-test attributes for stability
    @property
    def username_input(self):
        return self.page.locator("[data-test='username']")

    @property
    def password_input(self):
        return self.page.locator("[data-test='password']")

    @property
    def login_button(self):
        return self.page.locator("[data-test='login-button']")

    @property
    def error_message(self):
        return self.page.locator("[data-test='error']")

    def login(self, username: str, password: str) -> None:
        """Perform login with the given credentials."""
        self.goto()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        """Return the login error message text, or empty string if not visible."""
        return self.error_message.text_content() or ""
