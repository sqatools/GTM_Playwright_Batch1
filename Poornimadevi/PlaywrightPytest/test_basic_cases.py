import re
from playwright.sync_api import Page, expect


def test_facebook_login(page: Page):
    page.goto("https://www.facebook.com")
    expect(page).to_have_title(re.compile("facebook", re.IGNORECASE))
    page.get_by_test_id("royal-email").fill("user1@gmail.com")
    page.get_by_test_id("royal-pass").fill("user1234")
    page.get_by_test_id("royal-login-button1").click()
    element = page.get_by_text(re.compile("The password that you've entered is incorrect."))
    expect(element).to_be_visible(timeout=10_000)


def test_create_new_account_facebook(page: Page):
    page.goto("https://www.facebook.com/r.php?entry_point=login")
    page.get_by_label("First name").fill("John")
    page.get_by_label("Surname").fill("Deo")
    page.get_by_label("Day").select_option("20")
    page.get_by_label("Month").select_option("Dec")
    page.get_by_label("Year").select_option("1990")
    page.get_by_label("Female").click()
    page.get_by_label("Mobile number or email address").fill("987897987")
    page.get_by_label("New password").fill("user@12345")
    page.get_by_role("button", name='Sign Up')
