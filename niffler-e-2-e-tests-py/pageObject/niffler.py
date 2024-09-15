from pageObject.header import Header
from pageObject.login_page import LoginPage
from pageObject.welcome_page import WelcomePage


class Niff:
    def __init__(self, browser):
        self.browser = browser
        self.welcome_page = WelcomePage(self.browser)
        self.login_page = LoginPage(self.browser)
        self.header = Header(self.browser)

    def open(self, path: str):
        self.browser.open(path)
        return self
