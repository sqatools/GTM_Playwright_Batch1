import re
import re
from playwright.sync_api import Page, expect


# def test_Facebook_login(page: Page):
#     page.goto("https://www.facebook.com/")
#     expect(page).to_have_title(re.compile("facebook", re.IGNORECASE))
#     page.get_by_test_id("royal-email").fill("monthjuly@gmail.com")
#     page.get_by_label("Password").fill("123456")
#     page.get_by_id("login_link").click()
#     element = page.get_text(re.compile("The email you entered isn’t connected to an account. "))
#     expect(element).to_be_visible(timeout=10_000)


# def test_create_new_account(page: Page):
#     page.goto("https://www.facebook.com/r.php?locale=en_US&display=page&entry_point=login")
#     # page.get_role("button").click()
#     page.get_by_lable("First name").fill("Pyhon")
#     page.get_by_lable("Last name").fill("with playwright")
#     page.get_by_lable("Month").select_option("Jul")
#     page.get_by_lable("Day").select_option("27")
#     page.get_by_lable("Year").select_option("2020")
#     page.get_by_lable("Female").click()
#     page.get_by_lable("Mobile number or email").fill("47603848")
#     page.get_by_lable("New password").fill("newaccountcreated")
#     page.get_role("submit").click()
