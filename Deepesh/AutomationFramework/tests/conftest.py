import pytest
from playwright.sync_api import Page, Playwright, Browser, sync_playwright


@pytest.fixture(scope='class')
def get_page(request, page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.page = page
    yield
    page.close()


@pytest.fixture(scope='class')
def browser_context(request):
    with sync_playwright() as p:
        #browser: Browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=3000)
        browser: Browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="class")
def page_fixture(browser_context):
    page: Page = browser_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page
    page.close()
