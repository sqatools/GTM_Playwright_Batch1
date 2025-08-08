import time

import pytest
from page_objects.login_page import LoginPage
from page_objects.admin_page import AdminPage
from playwright.sync_api import Page, expect

#@pytest.mark.usefixtures("get_page")
class TestOpenHrmWebsite:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.lp = LoginPage(self.page)
        self.ad = AdminPage(self.page)

    def test_login_to_hrm_website(self):
        self.lp.launch_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp.login_to_hrm_website(user_name='Admin', pass_value='admin123')
        expect(self.lp.get_dashboard_heading()).to_be_visible()
        self.ad.navigate_to_admin_page()
        expect(self.ad.get_admin_heading()).to_be_visible()
        time.sleep(5)



