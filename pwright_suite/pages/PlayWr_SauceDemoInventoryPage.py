"""
Playwright SauceDemo Inventory Page
"""

class PW_SauceDemoInventory:

    def __init__(self, page):
        self.page = page
        self.inventory_container = page.locator(".inventory_container")
        self.shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_to_cart(self, product_name):
        card = self.page.locator(".inventory_item").filter(has_text=product_name)
        card.get_by_role("button", name="Add to cart").click()

    def remove_from_cart_btn(self, product_name):
        card = self.page.locator(".inventory_item").filter(has_text=product_name)
        return card.get_by_role("button", name="Remove")

    def go_to_cart(self):
        self.shopping_cart_link.click()



