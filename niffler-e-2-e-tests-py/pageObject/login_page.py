from selene.support.conditions import have
from selene.support.shared.jquery_style import s


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login_input(self, text):
        s('input[name="username"]').type(text)
        return self

    def password_input(self, text):
        s('input[name="password"]').type(text)
        return self

    @property
    def sign_in_btn(self):
        return s('.form__submit')

    @property
    def get_password_visible_btn(self):
        return s('.form__password-button')

    @property
    def form_error(self):
        return s('.form__error')
