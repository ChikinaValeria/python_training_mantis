import time
from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    """project_count = app.project.count()
    if project_count == 0:
        app.project.create_project(Project(name="test_name", description = "test_description"))"""
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    #app.wd.find_element('xpath', "/html/body/table[3]/tbody/tr[3]/td[1]/a").click()
    #app.wd.find_element('xpath', "//input[@value='Delete Project']").click()
    #time.sleep(1)
    #app.wd.find_element('xpath', "//input[@value='Delete Project']").click()

    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)