from playwright.sync_api import Playwright, sync_playwright, expect

# different pages in one browser context

with sync_playwright() as pw:
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    browser = pw.chromium.launch(headless=False, slow_mo=2000, executable_path=edge_path)
    context = browser.new_context()
    page = context.new_page()
    page1 = context.new_page()
    page.goto("https://www.facebook.com")
    page1.goto("https://www.bing.com/search?pglt=2083&q=google&cvid=e540179304b94ae699b70bedabec667d&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAuGEAyBggDEAAYQDIGCAQQLhhAMgYIBRAuGEAyBggGEC4YQDIGCAcQLhhAMgYICBAFGEAyCAgJEOkHGPxV0gEIMTQ2NWowajGoAgCwAgA&FORM=ANNAB1&PC=U531")
    page.get_by_test_id("royal-email").fill("user1@gmail.com")
    page.get_by_test_id("royal-pass").fill("user1@12345")
    page.get_by_test_id("royal-login-button").click()
    page1.locator("//textarea[@name='q']").fill("Playwright Testing")
    page1.get_by_label("Google Search").click()

    page.close()
    page1.close()
