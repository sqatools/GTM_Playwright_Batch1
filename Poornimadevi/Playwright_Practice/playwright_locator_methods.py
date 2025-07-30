import re

from playwright.sync_api import Page, Playwright, sync_playwright


"""
page.get_by_role() to locate by explicit and implicit accessibility attributes.
page.get_by_text() to locate by text content.
page.get_by_label() to locate a form control by associated label's text.
page.get_by_placeholder() to locate an input by placeholder.
page.get_by_alt_text() to locate an element, usually image, by its text alternative.
page.get_by_title() to locate an element by its title attribute.
page.get_by_test_id()
page.get_by_locator()
"""

def facebook_login():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.facebook.com")
        # get_by_test_id
        page.get_by_test_id("royal-email").fill("user1@gmail.com")
        page.get_by_test_id("royal-pass").fill("user@1234")
        # get_by_text
        # page.get_by_text("Log in").nth(1).click()

        # get_by_role()
        # page.get_by_role("button", name="Log in").click()

        # Identify the element with partial text value and ignore case sensitivity
        # page.get_by_role("button", name=re.compile("log", re.IGNORECASE)).click()

        # identify the element with XPATH locator
        # page.locator("//button[@name='login']").click()

        # identify the element with CSS selector
        page.locator("[name='login']").click()

        page.wait_for_timeout(timeout=10000)



#facebook_login()


def facebook_login_2():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.facebook.com")
        """
        # get_by_test_label,  This method we can use with arial-label attribute, or label tagname
        page.get_by_label("Email address or phone number").fill("user1@gmail.com")
        page.get_by_label("Password").fill("user1@1234")
        """
        """
        # get_by_test_label, with partial label value
        page.get_by_label(re.compile("email address", re.IGNORECASE)).fill("user1@gmail.com")
        page.get_by_label(re.compile("pass", re.IGNORECASE)).fill("user1@1234")
        """

        # get_by_placeholder
        page.get_by_placeholder("Email address or phone number").fill("user1@gmail.com")
        page.get_by_placeholder("Password").fill("user1@gmail.com")

        # get image element with alt attribute
        page.get_by_alt_text("Facebook").click()



        page.wait_for_timeout(timeout=10000)

facebook_login_2()