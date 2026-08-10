"""
Playwright Heroku login page
"""

class PlyWr_HerokuLogin:

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def load(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()
