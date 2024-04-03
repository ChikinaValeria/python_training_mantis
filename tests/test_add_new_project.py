import random
from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.project.get_project_list()
    #print(old_projects)
    project_name = ("Project_test " + str(random.randint(0, 100)))
    project_description = ("Description_test " + str(random.randint(0, 100)))
    app.project.create_project(Project(name=project_name, description = project_description))
    old_projects.append(Project(name=project_name, description = project_description))
    #print("old projects appended", old_projects)
    new_projects = app.project.get_project_list()
    #print("new projects", new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


