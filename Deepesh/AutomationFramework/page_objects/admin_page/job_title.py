import re


class JobTitle:
    def __init__(self, page):
        self.page = page

    def navigate_to_job_title(self):
        self.page.locator("//span[normalize-space()='Job']//parent::li").click()
        self.page.locator("//a[normalize-space()='Job Titles']//parent::li").click()

    def add_job_title(self, job_title, job_desc, file_path, notes):
        self.page.get_by_role("button", name=re.compile("Add")).click()
        self.page.locator("//label[text()='Job Title']//parent::div//following-sibling::div//input").fill(job_title)
        self.page.locator("//label[text()='Job Description']//parent::div//following-sibling::div//textarea").fill(job_desc)
        self.page.locator("//input[@type='file']").set_input_files(file_path)
        self.page.get_by_placeholder("Add note").fill(notes)
        self.page.get_by_role("button", name=re.compile("Save")).click()

