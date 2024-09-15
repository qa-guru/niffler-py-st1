import os
from dotenv import load_dotenv

load_dotenv()

from selene import be


def test_login(niff):
    niff.open('/main')
    niff.welcome_page.should_have_text('Welcome to magic journey with Niffler. The coin keeper')
    niff.welcome_page.login_btn.click()
    niff.login_page.login_input(os.getenv('WEB_LOGIN'))
    niff.login_page.password_input(os.getenv('WEB_PASS'))
    niff.login_page.sign_in_btn.click()
    niff.header.header_text.should(be.visible)


def test_login_negative(niff):
    niff.open('/main')
    niff.welcome_page.login_btn.click()
    niff.login_page.login_input('randomname')
    niff.login_page.password_input('12311234124')
    niff.login_page.sign_in_btn.click()
    niff.login_page.form_error.should(be.visible)