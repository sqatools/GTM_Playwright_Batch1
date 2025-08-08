import pytest
from playwright.sync_api import Page, Playwright, Browser

@pytest.fixture(scope='class')
def get_page(request, page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.page = page
    yield
    page.close()

