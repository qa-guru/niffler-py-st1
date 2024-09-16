import pytest
from selene.support.shared import browser as selene_browser
from pageObject.niffler import Niff


@pytest.fixture
def niff():
    selene_browser.config.base_url = "http://frontend.niffler.dc"
    niff = Niff(selene_browser)
    yield niff
    selene_browser.quit()
