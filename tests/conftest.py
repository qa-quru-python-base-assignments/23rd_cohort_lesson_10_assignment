import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
