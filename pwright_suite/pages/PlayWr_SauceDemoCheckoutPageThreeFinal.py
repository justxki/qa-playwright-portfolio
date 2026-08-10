"""
Playwright SauceDemo Checkout Page Three // Confirmation Page
"""

class PW_SauceDemoCheckoutThreeFinal:

    def __init__(self, page):
        self.page = page
        self.order_conf_header = page.get_by_role("heading", name="Thank you for your order!", level=2)
        self.shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")
