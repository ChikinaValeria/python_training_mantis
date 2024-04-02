

class Project_helper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php')

    def fill_project_form(self, project_name, project_description):
        wd = self.app.wd
        wd.find_element('name', "name").click()
        wd.find_element('name', "name").clear()
        wd.find_element('name', "name").send_keys("project_name")
        wd.find_element('name', "description").click()
        wd.find_element('name', "description").clear()
        wd.find_element('name', "description").send_keys("project_description")


    def create_project(self, project_name, project_description):
        wd = self.app.wd
        self.fill_project_form(project_name, project_description)
        wd.find_element('xpath', "//input[@value='Add Project']").click()





    """def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element('link text', "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element('name', "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element('name', "submit").click()
        self.return_to_groups_page()
        # сброс кэша, который стал невалиден после создания нового объекта
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)"""