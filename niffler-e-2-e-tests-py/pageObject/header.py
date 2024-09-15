from selene.support.shared.jquery_style import s
from selene import have, be


class Header:
    def __init__(self, browser):
        self.browser = browser

    @property
    def header_text(self):
        return s('h1').should(have.text('Niffler. The coin keeper.'))
