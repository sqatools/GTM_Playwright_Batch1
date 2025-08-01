from playwright.sync_api import Playwright, sync_playwright, expect

# different pages in one browser context
def execute_code_with_different_page_on_same_browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        page1 = context.new_page()
        page.goto("https://www.facebook.com")
        page1.goto("https://www.google.co.in/")
        page.get_by_test_id("royal-email").fill("user1@gmail.com")
        page.get_by_test_id("royal-pass").fill("user1@12345")
        page.get_by_test_id("royal-login-button").click()
        page1.locator("//textarea[@name='q']").fill("Playwright Testing")
        page1.get_by_label("Google Search").click()

        page.close()
        page1.close()

execute_code_with_different_page_on_same_browser()

def execute_code_with_different_page_on_diff_browser_instance():
# different browser context
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=2000)
        context1 = browser.new_context()
        context2 = browser.new_context()
        page = context1.new_page()
        page1 = context2.new_page()
        page.goto("https://www.facebook.com")
        page1.goto("https://www.google.co.in/")
        page.get_by_test_id("royal-email").fill("user1@gmail.com")
        page.get_by_test_id("royal-pass").fill("user1@12345")
        page.get_by_test_id("royal-login-button").click()
        page1.locator("//textarea[@name='q']").fill("Playwright Testing")
        page1.get_by_label("Google Search").click()

        page.close()
        page1.close()
