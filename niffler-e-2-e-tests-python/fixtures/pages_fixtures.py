import pytest
from selene import browser


@pytest.fixture()
def main_page(auth_token, envs):
    browser.open(envs.frontend_url)
