"""
Pytest fixtures for Playwright E2E tests.

Demonstrates:
- page fixture from pytest-playwright (browser, context, page)
- Custom fixtures for page objects and authenticated session
- Trace on failure is enabled via pytest.ini (--tracing retain-on-failure)
- Retries: use pytest-rerunfailures and run with --reruns 1 if desired
"""

import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# ---------------------------------------------------------------------------
# Page object fixtures: one per page for clear, reusable test setup
# ---------------------------------------------------------------------------


@pytest.fixture
def login_page(page):
    """Login page object bound to the current Playwright page."""
    return LoginPage(page)


@pytest.fixture
def products_page(page):
    """Products (inventory) page object."""
    return ProductsPage(page)


@pytest.fixture
def cart_page(page):
    """Cart page object."""
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    """Checkout page object (step one and two)."""
    return CheckoutPage(page)


# ---------------------------------------------------------------------------
# Flow fixture: logged-in session at products page (for cart/checkout tests)
# ---------------------------------------------------------------------------

# Saucedemo demo credentials
DEMO_USER = "standard_user"
DEMO_PASSWORD = "secret_sauce"


@pytest.fixture
def logged_in_page(login_page, products_page):
    """
    Perform login and return the products page object.
    Use for tests that start from the product list (cart, checkout flows).
    """
    login_page.login(DEMO_USER, DEMO_PASSWORD)
    # After login we're on inventory; ensure products page is ready
    products_page.inventory_list.wait_for(state="visible", timeout=10000)
    return products_page
