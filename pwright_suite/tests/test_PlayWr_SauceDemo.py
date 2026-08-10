"""
Playwright SauceDemo Test Page
"""
from playwright.sync_api import expect
from pwright_suite.pages.PlayWr_SauceDemoLoginPage import PW_SauceDemoLogin
from pwright_suite.pages.PlayWr_SauceDemoInventoryPage import PW_SauceDemoInventory
from pwright_suite.pages.PlayWr_SauceDemoCartPage import PW_SauceDemoCart
from pwright_suite.pages.PlayWr_SauceDemoCheckoutPageOne import PW_SauceDemoCheckoutOne
from pwright_suite.pages.PlayWr_SauceDemoCheckoutPageTwo import PW_SauceDemoCheckoutTwo
from pwright_suite.pages.PlayWr_SauceDemoCheckoutPageThreeFinal import PW_SauceDemoCheckoutThreeFinal

def test_saucedemo(page):
    login_page = PW_SauceDemoLogin(page)
    inventory_page = PW_SauceDemoInventory(page)
    cart_page = PW_SauceDemoCart(page)
    checkout_one = PW_SauceDemoCheckoutOne(page)
    checkout_two = PW_SauceDemoCheckoutTwo(page)
    checkout_three = PW_SauceDemoCheckoutThreeFinal(page)

    login_page.load()
    expect(page).to_have_url("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory_page.inventory_container).to_be_visible()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.shopping_cart_badge).to_be_visible()
    expect(inventory_page.remove_from_cart_btn("Sauce Labs Backpack")).to_be_visible()
    inventory_page.go_to_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.cart_container).to_be_visible()
    expect(cart_page.cart_items).not_to_have_count(0)
    cart_page.checkout_from_cart()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_one.input_and_continue("John", "Smith", "00000")

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout_two.checkout_overview_container).to_be_visible()
    expect(checkout_two.total_checkout_price).to_contain_text("$")
    checkout_two.finish_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_three.order_conf_header).to_contain_text("Thank you for your order!")
    expect(checkout_three.shopping_cart_badge).to_be_hidden()



