import re

from playwright.sync_api import Page, expect

def test_fb_login(page: Page):
    page.goto("https://www.facebook.com/r.php?entry_point=login")
    page.get_by_label("First name").fill("Varrinder")
    page.get_by_label("Last name").fill("Kaur")
    page.get_by_label("Month").select_option("Jul")
    page.get_by_label("Day").select_option("26")
    page.get_by_label("Year").select_option("2012")
    page.get_by_label("Female").click()
    page.get_by_label("Mobile number or email").fill("7034013740")
    page.get_by_label("New password").fill("Summer2025!")
    page.get_by_title("Sign Up").click()

    #page.get_by_locator()





