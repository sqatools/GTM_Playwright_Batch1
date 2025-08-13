import re


class JobTitle:
    def __init__(self, page):
        self.page = page

    def navigate_to_job_title(self):
        self.page.locator("//span[normalize-space()='Job']//parent::li").click()
        self.page.locator("//a[normalize-space()='Job Titles']//parent::li").click()


