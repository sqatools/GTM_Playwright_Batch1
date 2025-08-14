import re
import time

import pytest
from playwright.sync_api import Page, expect
from user_input_data import *


class TestSelectDropDown:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_verify_select_dropdown_value(self):
        self.page.goto("https://demo.mobiscroll.com/jquery/select/group-options#")
        self.page.get_by_placeholder(re.compile("Please select")).click()
        self.page.get_by_text("Camera and Photo").click()
        self.page.get_by_text("Cell Phones").click()
        self.page.get_by_text("GPS and Navigation").click()
        time.sleep(5)


