from selenium.webdriver.common.by import By
from model.project import Project

class Project_helper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php')

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

    def delete_project_by_id(self):
        pass
    """def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements(By.XPATH, '//table[@class="width100"][2]//tbody//tr//class="row-"[1:]'))
        #return len(wd.find_elements('name', "selected[]"))



    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.open_project_page_by_link()
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s" % project.project_id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(0.5)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()"""

    """def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                # text = element.find_element('name', "selected[]").get_attribute("title")
                text = element.text
                id = element.find_element('name', "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        # print(self.group_cache)
        return list(self.group_cache)"""

    """def get_projects_list(self):
        wd = self.app.wd
        self.open_manage_projects()
        list = []
        count = len(wd.find_elements_by_xpath('//table[@class="width100"][2]//tbody//tr'))
        try:
            for n in range(3, count + 1):
                id = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').get_attribute(
                    'href')
                id = str(id).split("=")[1]
                name = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').text
                status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[2]').text
                enabled = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[3]').text
                view_status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[4]').text
                description = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[5]').text
                list.append(Project(id=id, name=name, status=status, enabled=enabled, view_status=view_status,
                                    description=description))
            return list
        except:
            return list
"""






