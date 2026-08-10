# QA Playwright Portfolio

Automated end-to-end tests for practice sites using Playwright + Pytest (Python).

## Sites Covered

- **SauceDemo** — full purchase flow (login → add to cart → 3-page checkout → order confirmation)
- **The Internet (Heroku)** — login authentication flow

## Tech Stack

- Python 3.x
- Playwright
- Pytest / pytest-playwright
- Page Object Model (POM) architecture

## Project Structure
```
pwright_suite/
├── pages/          # Page Object Models
└── tests/          # Test files + conftest.py
```

## Setup

```bash
# clone the repo
git clone https://github.com/justxki/qa-playwright-portfolio.git
cd qa-playwright-portfolio

# create venv
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# install dependencies
pip install playwright pytest-playwright
playwright install
```

## Running Tests

```bash
# run all tests
pytest

# run a specific test file
pytest pwright_suite/tests/test_PlayWr_SauceDemo.py

# run with browser visible (headed mode)
pytest --headed
```

## Highlights

- Semantic locators (`get_by_role`, `get_by_placeholder`) preferred over CSS/XPath for resilience
- `expect()` web-first assertions with auto-waiting
- Parametrized methods for repeated components (e.g., `add_to_cart(product_name)`)
- Page Object Model separating locators/actions from test logic
- URL and visibility assertions at every navigation step

## Also See

[qa-selenium-portfolio](https://github.com/justxki/qa-selenium-portfolio) — same testing approach implemented in Selenium for framework comparison.