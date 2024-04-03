import random
from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project_name = ("Project_test " + str(random.randint(0, 100)))
    project_description = ("Description_test " + str(random.randint(0, 100)))
    app.project.create_project(Project(name=project_name, description = project_description))
    old_projects.append(Project(name=project_name, description = project_description))
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


