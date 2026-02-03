"""
Product list E2E tests.

Covers: product list visible after login, add to cart updates badge.
Uses logged_in_page fixture for tests that start from inventory.
"""

import pytest


class TestProductList:
    """Tests for the Saucedemo product/inventory page."""

    def test_product_list_visible_after_login(self, logged_in_page):
        """After login, inventory list is visible and has items."""
        products_page = logged_in_page
        products_page.inventory_list.wait_for(state="visible", timeout=5000)
        items = products_page.get_product_items()
        assert items.count() >= 1

    def test_add_to_cart_increments_badge(self, logged_in_page):
        """Adding one product to cart shows cart badge count 1."""
        products_page = logged_in_page
        assert products_page.get_cart_count() == 0
        products_page.add_first_product_to_cart()
        assert products_page.get_cart_count() == 1

    def test_add_multiple_items_updates_badge(self, logged_in_page):
        """Adding two products updates cart badge to 2."""
        products_page = logged_in_page
        products_page.add_first_product_to_cart()
        # Second item: use "Add to cart" on another product
        products_page.get_product_items().nth(1).get_by_role("button", name="Add to cart").click()
        assert products_page.get_cart_count() == 2
