"""Cart page: review items and proceed to checkout."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Saucedemo cart page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, "cart.html")

    @property
    def checkout_button(self):
        return self.page.locator("[data-test='checkout']")

    @property
    def cart_items(self):
        return self.page.locator("[data-test='inventory-item']")

    def get_item_count(self) -> int:
        """Return the number of items in the cart."""
        return self.cart_items.count()

    def proceed_to_checkout(self) -> None:
        """Click Checkout to go to the checkout information step."""
        self.checkout_button.click()
