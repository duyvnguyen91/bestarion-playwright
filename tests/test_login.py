"""
Login flow E2E tests.

Covers: successful login, invalid credentials, empty fields.
Uses fixtures (login_page) and stable selectors (data-test).
"""

import pytest

from pages.base_page import BASE_URL


class TestLoginFlow:
    """Tests for the Saucedemo login page."""

    def test_successful_login_lands_on_products(self, login_page, products_page):
        """Valid credentials redirect to the product list."""
        login_page.login("standard_user", "secret_sauce")
        products_page.inventory_list.wait_for(state="visible", timeout=10000)
        assert products_page.page.url.startswith(f"{BASE_URL}/inventory")

    def test_invalid_password_shows_error(self, login_page):
        """Wrong password shows error and stays on login page."""
        login_page.login("standard_user", "wrong_password")
        assert "Epic sadface: Username and password do not match" in login_page.get_error_text()
        assert login_page.page.url.rstrip("/").endswith("saucedemo.com")

    def test_locked_user_shows_error(self, login_page):
        """Locked out user sees specific error message."""
        login_page.login("locked_out_user", "secret_sauce")
        assert "locked out" in login_page.get_error_text().lower()

    def test_empty_username_shows_error(self, login_page):
        """Submitting with empty username shows validation error."""
        login_page.login("", "secret_sauce")
        assert len(login_page.get_error_text()) > 0

    def test_empty_password_shows_error(self, login_page):
        """Submitting with empty password shows validation error."""
        login_page.login("standard_user", "")
        assert len(login_page.get_error_text()) > 0
