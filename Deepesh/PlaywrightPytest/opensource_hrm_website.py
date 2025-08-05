import time

import pytest
from playwright.sync_api import Page, expect
from user_input_data import *


class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page


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
