import time


class LoginPage:
    def __init__(self, page):
        self.page = page

    def launch_login_page(self, url):
        self.page.goto(url)

    def enter_username(self, user_name_value):
        self.page.get_by_placeholder("Username").fill(user_name_value)

    def enter_password(self, pass_value):
        self.page.get_by_placeholder("password").fill(pass_value)

    def click_on_login_button(self):
        self.page.get_by_role("button", name="Login").click()

    def get_dashboard_heading(self):
        return self.page.get_by_role("heading", name="Dashboard")

    def login_to_hrm_website(self, user_name, pass_value):
        self.enter_username(user_name)
        self.enter_password(pass_value)
        self.click_on_login_button()
        time.sleep(5)
