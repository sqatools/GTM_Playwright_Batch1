import re


class AdminPage:
    def __init__(self, page):
        self.page = page


    def navigate_to_admin_page(self):
        self.page.get_by_role("link", name="Admin").click()

    def get_admin_heading(self):
        return self.page.get_by_role("heading", name=re.compile("User Management"))
