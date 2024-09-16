from selene import browser


class BasePage:
    def open(self, path: str):
        browser.open_url(path)
        return self
