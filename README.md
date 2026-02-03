# Playwright Demo Project (Python)

A practical end-to-end test suite using **Playwright** and **Python**, targeting [Saucedemo](https://www.saucedemo.com/). Built to demonstrate good practices for portfolio, interview demos, and future CI integration.

## Goals

- **Real user flows:** Login, product list, cart, and checkout
- **Clean structure:** Page Object Model and pytest fixtures
- **Good Playwright practices:** Fixtures, stable selectors, retries, traces

## What’s Covered

| Area           | Description                                      |
|----------------|--------------------------------------------------|
| **Login flow** | Valid/invalid credentials, locked user, empty fields |
| **Product list** | Inventory visible after login, add to cart, badge count |
| **Cart & checkout** | Cart contents, checkout info step, full order completion |

## Tech Stack

- **Python 3**
- **Playwright** (browser automation)
- **pytest** + **pytest-playwright** (runner and fixtures)

## Setup

1. **Create a virtual environment (recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers (one-time):**

   ```bash
   playwright install chromium
   ```

   For all browsers: `playwright install`

## Running Tests

From the project root:

```bash
# Run all tests (Chromium, with retries and trace on failure)
pytest

# Run with visible browser
pytest --headed

# Run a specific file or test
pytest tests/test_login.py
pytest tests/test_login.py::TestLoginFlow::test_successful_login_lands_on_products

# Other browsers
pytest --browser firefox
pytest --browser webkit

# Disable retries when debugging
pytest --retries=0

# Record trace for every test
pytest --tracing=on
```

## Configuration (pytest.ini)

- **Retries:** `--retries=1` (retry failed tests once; useful for CI)
- **Traces:** `--tracing=retain-on-failure` (save trace when a test fails)
- **Browser:** `--browser chromium` (override with `--browser firefox` or `webkit`)

## Viewing Traces

After a failure, traces are under `test-results/`. To open a trace:

```bash
playwright show-trace test-results/<test-name>/trace.zip
```

Or upload `trace.zip` to [trace.playwright.dev](https://trace.playwright.dev).

## Project Structure

```
bestarion-playwright/
├── conftest.py          # Pytest fixtures (page objects, logged_in_page)
├── pytest.ini           # Retries, traces, browser
├── requirements.txt
├── pages/               # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
└── tests/
    ├── test_login.py
    ├── test_product_list.py
    └── test_cart_checkout.py
```

## Practices Demonstrated

- **Fixtures:** `login_page`, `products_page`, `cart_page`, `checkout_page`, `logged_in_page`
- **Selectors:** `data-test` attributes for stability
- **Retries:** Configured in `pytest.ini` for flaky resilience
- **Traces:** `retain-on-failure` for debugging failed runs

## License

MIT
