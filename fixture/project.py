from selenium.webdriver.common.by import By
from model.project import Project
import time
class Project_helper:

    def __init__(self, app):
        self.app = app


    def open_project_page(self):
        wd = self.app.wd
        wd.get(self.app.project_url)

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element('name', "name").click()
        wd.find_element('name', "name").clear()
        wd.find_element('name', "name").send_keys(project.name)
        wd.find_element('name', "description").click()
        wd.find_element('name', "description").clear()
        wd.find_element('name', "description").send_keys(project.description)


    def submit_project(self):
        wd = self.app.wd
        wd.find_element('xpath', "//input[@value='Add Project']").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element('xpath', "//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        self.submit_project()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        list = []
        count = len(wd.find_elements(By.XPATH, '//table[@class="width100"][2]//tbody//tr'))
        for i in range(3, count + 1):
            project_id = wd.find_element(By.XPATH,
                f'//table[@class="width100"][2]//tbody//tr[{i}]//td//a').get_attribute('href')
            project_id = str(project_id).split("=")[1]
            project_name = wd.find_element(By.XPATH, f'//table[@class="width100"][2]//tbody//tr[{i}]//td//a').text
            list.append(Project(name =project_name, id=project_id))
        return list

    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='manage_proj_edit_page.php?project_id=%s" % project.id).click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()












