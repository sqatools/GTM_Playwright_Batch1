import os
import time

import pytest
from ..page_objects.loging_page.login_page import LoginPage
from ..page_objects.admin_page.add_user import AddUser
from ..page_objects.admin_page.job_title import JobTitle
from ..utilities.util_tools import Utils
from playwright.sync_api import expect


@pytest.mark.usefixtures("page_fixture")
class TestOpenHrmWebsite:

    @pytest.fixture(autouse=True)
    def setup(self, page_fixture):
        self.page = page_fixture
        self.lp = LoginPage(self.page)
        self.ad = AddUser(self.page)
        self.jb = JobTitle(self.page)
        self.util = Utils()
        self.data_file_path = os.path.join(os.getcwd(), "resource_data/test_input_data.json")
        self.excel_file = os.path.join(os.getcwd(), "resource_data/test_data.xlsx")
        self.data = self.util.read_json_data(self.data_file_path)

    def test_login_to_hrm_website(self):
        self.lp.login_to_hrm_website(user_name='Admin', pass_value='admin123')
        expect(self.lp.get_dashboard_heading()).to_be_visible()

    @pytest.mark.skip
    def test_admin_verify_operation(self):
        self.ad.navigate_to_admin_page()
        expect(self.ad.get_admin_heading()).to_be_visible()
        time.sleep(5)
        self.ad.add_user_operation(user_role=self.data['AdminPage']['AddUser']['user_role'],
                                   user_status=self.data['AdminPage']['AddUser']['user_status'],
                                   emp_name=self.data['AdminPage']['AddUser']['employee_name'],
                                   username=self.data['AdminPage']['AddUser']['emp_username'],
                                   password=self.data['AdminPage']['AddUser']['password'],
                                   conf_pass=self.data['AdminPage']['AddUser']['password'])
        time.sleep(5)

    def test_add_job_title_and_verify(self):
        self.ad.navigate_to_admin_page()
        expect(self.ad.get_admin_heading()).to_be_visible()
        self.jb.navigate_to_job_title()
        self.jb.add_job_title(job_title=self.util.read_excel_file(self.excel_file, "Sheet1", "B2"),
                              job_desc=self.util.read_excel_file(self.excel_file, "Sheet1", "B3"),
                              file_path=self.util.read_excel_file(self.excel_file, "Sheet1", "B4"),
                              notes=self.util.read_excel_file(self.excel_file, "Sheet1", "B5"))
        time.sleep(5)

