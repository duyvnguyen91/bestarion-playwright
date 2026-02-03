"""Products (inventory) page: product list and add-to-cart actions."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Saucedemo products/inventory page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, "inventory.html")

    @property
    def inventory_list(self):
        return self.page.locator("[data-test='inventory-list']")

    @property
    def cart_link(self):
        return self.page.locator("[data-test='shopping-cart-link']")

    @property
    def cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")

    def get_product_items(self):
        """Return locator for all inventory items (each item has add-to-cart button)."""
        return self.page.locator("[data-test='inventory-item']")

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        """Add to cart the product with the given display name."""
        item = self.get_product_items().filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def add_first_product_to_cart(self) -> None:
        """Add the first product in the list to the cart."""
        self.get_product_items().first.get_by_role("button", name="Add to cart").click()

    def get_cart_count(self) -> int:
        """Return the number shown on the cart badge, or 0 if no badge."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content() or "0")
        return 0

    def open_cart(self) -> None:
        """Click the cart icon to go to the cart page."""
        self.cart_link.click()
