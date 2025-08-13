import re


class AddUser:
    def __init__(self, page):
        self.page = page

    def navigate_to_admin_page(self):
        self.page.get_by_role("link", name="Admin").click()

    def get_admin_heading(self):
        return self.page.get_by_role("heading", name=re.compile("User Management"))

    def click_to_add_user_button(self):
        self.page.get_by_text("Add").click()

    def select_user_role(self, user_role):
        self.page.locator(
            "//label[text()='User Role']//parent::div//following-sibling::div//div[contains(text(), 'Select')]").click()
        self.page.locator(f"//div[@role='listbox']//*[contains(text(), '{user_role}')]").click()

    def select_user_status(self, user_status):
        self.page.locator(
            "//label[text()='Status']//parent::div//following-sibling::div//div[contains(text(), 'Select')]").click()
        self.page.locator(f"//div[@role='listbox']//*[contains(text(), '{user_status}')]").click()

    def select_employee(self, emp_name):
        self.page.get_by_placeholder(re.compile("Type for hints")).fill(emp_name)
        self.page.locator(f"//*[contains(text(), '{emp_name}')]").click()

    def enter_emp_username(self, emp_username):
        self.page.locator("//label[text()='Username']//parent::div//following-sibling::div/input").fill(emp_username)

    def enter_password(self, password):
        self.page.locator("//label[text()='Password']//parent::div//following-sibling::div/input").fill(password)

    def enter_confirm_password(self, conf_password):
        self.page.locator("//label[text()='Confirm Password']//parent::div//following-sibling::div/input").fill(
            conf_password)

    def click_on_save_button(self):
        self.page.get_by_role("button", name="Save").click()

    def add_user_operation(self, user_role, user_status, emp_name, username, password, conf_pass):
        self.click_to_add_user_button()
        self.select_user_role(user_role)
        self.select_user_status(user_status)
        self.select_employee(emp_name)
        self.enter_emp_username(username)
        self.enter_password(password)
        self.enter_confirm_password(conf_pass)
        self.click_on_save_button()
