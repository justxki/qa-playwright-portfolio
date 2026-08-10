"""
SauceDemo Login Page
"""

class PW_SauceDemoLogin:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_btn = page.locator("[data-test='login-button']")

    def load(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

