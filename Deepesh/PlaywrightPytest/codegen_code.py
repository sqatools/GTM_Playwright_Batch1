import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nseindia.com/")
    page.get_by_text("Market Turnover", exact=True).click()
    page.get_by_role("cell", name="1,50,870").dblclick()
    page.get_by_role("button", name="Close").click()
    page.get_by_text("Advances", exact=True).dblclick()
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="1,932").dblclick()
    page2 = page2_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
