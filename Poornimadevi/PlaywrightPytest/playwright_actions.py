import time

import pytest
from playwright.sync_api import Page, expect
from user_input_data import *


class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    @pytest.mark.skip
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
        time.sleep(5)
        # upload file from current location
        #self.page.locator("#myFile").set_input_files("user_input_data.py")

        # upload file from any specific target path
        self.page.locator("#myFile").set_input_files(r"E:\Filesdata\count_name.txt")
        time.sleep(5)
        self.page.locator("//form/input[@type='submit']").click()
        time.sleep(5)


    def test_execute_radio_checkbox(self):
        self.page.goto("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

        # radio button status
        element = self.page.locator("#oneway")
        print("radio status :", element.is_checked())
        element.set_checked(True)
        print("radio status after check :", element.is_checked())

        # checkbox elements list
        checkbox_list = self.page.locator("//input[@type='checkbox']").all()
        for checkbox in checkbox_list:
            print("before check :", checkbox.is_checked())
            checkbox.set_checked(True)
            print("after check :", checkbox.is_checked())
            print("_"*50)


    def test_drag_drop_operation(self):
        self.page.goto("https://www.globalsqa.com/demo-site/draganddrop/")
        frame_element = self.page.frame_locator("//iframe[contains(@aria-label, 'To enrich screen reader')]")
        frame_element.get_by_text("High Tatras").drag_to(self.page.locator("#trash"))
        time.sleep(5)













