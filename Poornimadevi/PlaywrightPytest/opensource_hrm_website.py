import time

import pytest
from playwright.sync_api import Page, expect
from user_input_data import *


class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page


    @pytest.mark.skip
    def test_login_functionality(self):
        #self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.goto("/web/index.php/auth/login")
        self.page.get_by_placeholder("Username").fill(TestData.username)
        self.page.get_by_placeholder("Password").fill(TestData.password)
        self.page.get_by_role("button", name="Login").click()
        self.page.get_by_text("Admin").click()
        self.page.locator("//label[text()='Username']//following::input[contains(@class, 'oxd-input--active')]").fill(
            TestData.username)

        self.page.locator("(//label[text()='User Role']//following::div[@class='oxd-select-text-input'])[1]").click()

        self.page.locator("//div[@role='listbox']//*[contains(text(), 'Admin')]").click()
        time.sleep(10)


    def test_verify_select_dropdown_value(self):
        self.page.goto("https://sqatools.in/dummy-booking-website/")

        # select value by label
        # self.page.locator("#admorepass").select_option(label="Add 2 more passenger (200%)")
        # self.page.locator("#billing_country").select_option(label="Barbados")

        # select value by index
        # self.page.locator("#admorepass").select_option(index=3)
        # self.page.locator("#billing_country").select_option(index=4)

        # select by value
        self.page.locator("#admorepass").select_option(value="3")
        self.page.locator("#billing_country").select_option(value="AQ")

        # If multiple values are to select
        # self.page.locator("#billing_country").select_option(['Mango', 'Banana', 'Apple'])

        # perform keyboard key operation : select all content of the page
        self.page.locator("#billing_country").press("Control+A")
        time.sleep(5)

        # open developer tool
        self.page.locator("#billing_country").press("F12")
        time.sleep(5)

        """
        Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
         ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
         ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.
        
        """

    def test_upload_a_file(self):
        self.page.goto("https://automationbysqatools.blogspot.com/2020/08/login.html")






