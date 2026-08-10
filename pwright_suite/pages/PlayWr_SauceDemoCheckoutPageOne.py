"""
Playwright SauceDemo Checkout Page One
"""

class PW_SauceDemoCheckoutOne:

    def __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_checkout_btn = page.get_by_role("button", name="Continue")

    def input_and_continue(self, first, last, postal):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.postal_input.fill(postal)
        self.continue_checkout_btn.click()

