"""
Cart and checkout E2E tests.

Full flow: login -> add to cart -> cart -> checkout (info + overview) -> finish.
Demonstrates E2E storytelling and reuse of page objects and fixtures.
"""

import pytest


class TestCartAndCheckout:
    """Tests for cart and checkout flows on Saucedemo."""

    def test_cart_shows_added_item(self, logged_in_page, cart_page):
        """After adding one product, cart page shows one item."""
        products_page = logged_in_page
        products_page.add_first_product_to_cart()
        products_page.open_cart()
        assert cart_page.get_item_count() == 1

    def test_checkout_requires_information(self, logged_in_page, cart_page, checkout_page):
        """From cart, checkout leads to information step."""
        products_page = logged_in_page
        products_page.add_first_product_to_cart()
        products_page.open_cart()
        cart_page.proceed_to_checkout()
        checkout_page.first_name_input.wait_for(state="visible", timeout=5000)
        assert checkout_page.first_name_input.is_visible()

    def test_full_checkout_flow_completes_order(
        self, logged_in_page, cart_page, checkout_page
    ):
        """E2E: Login -> add to cart -> checkout with info -> finish -> thank you."""
        products_page = logged_in_page
        products_page.add_first_product_to_cart()
        products_page.open_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_information("Jane", "Doe", "12345")
        checkout_page.finish_checkout()

        assert checkout_page.is_order_complete()
