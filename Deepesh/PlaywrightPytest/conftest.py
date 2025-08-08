from playwright.sync_api import Page
import pytest

@pytest.fixture(scope='class')
def class_setup(page: Page, request):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.page = page
    yield page