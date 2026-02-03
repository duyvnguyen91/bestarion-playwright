"""Checkout flow: information step and overview/finish."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Saucedemo checkout: info (step one) and overview/finish (step two)."""

    def __init__(self, page: Page) -> None:
        # Checkout uses checkout-step-one.html and checkout-step-two.html
        super().__init__(page, "checkout-step-one.html")

    # Step one: customer information
    @property
    def first_name_input(self):
        return self.page.locator("[data-test='firstName']")

    @property
    def last_name_input(self):
        return self.page.locator("[data-test='lastName']")

    @property
    def postal_code_input(self):
        return self.page.locator("[data-test='postalCode']")

    @property
    def continue_button(self):
        return self.page.locator("[data-test='continue']")

    # Step two: overview and finish
    @property
    def finish_button(self):
        return self.page.locator("[data-test='finish']")

    @property
    def complete_header(self):
        return self.page.get_by_role("heading", name="Thank you for your order!")

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill checkout step one and continue."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self) -> None:
        """Click Finish on the overview step."""
        self.finish_button.click()

    def is_order_complete(self) -> bool:
        """Return True if the 'Thank you' confirmation is visible."""
        return self.complete_header.is_visible()
