from selene.support.shared.jquery_style import s
from selene import have, be


class WelcomePage:
    def __init__(self, browser):
        self.browser = browser

    def should_have_text(self, expected_text: str):
        s('h1').should(have.text(expected_text))
        return self

    @property
    def login_btn(self):
        return s('a.main__link[href="/redirect"]').should(be.visible)

    @property
    def register_btn(self):
        return s('a.main__link[href="/register"]')
