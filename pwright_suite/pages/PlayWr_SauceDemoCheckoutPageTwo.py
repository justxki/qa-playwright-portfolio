"""
Playwright SauceDemo Checkout Page Two
"""

class PW_SauceDemoCheckoutTwo:

    def __init__(self, page):
        self.page = page
        self.checkout_overview_container = page.locator("[data-test='checkout-summary-container']")
        self.total_checkout_price = page.locator("[data-test='total-label']")
        self.finish_checkout_btn = page.get_by_role("button", name="Finish")

    def finish_checkout(self):
        self.finish_checkout_btn.click()