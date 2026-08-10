"""
Playwright SauceDemo Cart Page
"""

class PW_SauceDemoCart:

    def __init__(self, page):
        self.page = page
        self.cart_container = page.locator("[data-test='cart-contents-container']")
        self.cart_items = page.locator(".cart_item")
        self.checkout_btn = page.get_by_role("button", name="Checkout")

    def checkout_from_cart(self):
        self.checkout_btn.click()

