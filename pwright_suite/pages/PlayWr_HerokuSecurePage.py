"""
Playwright Heroku secure page
"""

class PlyWr_HerokuSecure:

    def __init__(self, page):
        self.page = page
        self.banner = page.get_by_text("You logged into a secure area!")


