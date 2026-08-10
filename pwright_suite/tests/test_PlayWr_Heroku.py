"""
Playwright Heroku test page
"""

from playwright.sync_api import expect

from pwright_suite.pages.PlayWr_HerokuLoginPage import PlyWr_HerokuLogin
from pwright_suite.pages.PlayWr_HerokuSecurePage import PlyWr_HerokuSecure


def test_heroku_login(page):
    login_page = PlyWr_HerokuLogin(page)
    secure_page = PlyWr_HerokuSecure(page)

    login_page.load()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(secure_page.banner).to_be_visible()



