import random
from model.project import Project

def test_add_project_soap(app):
    old_projects = app.soap.get_project_list()
    print("Old_projects: ", old_projects)
    project_name = ("Project_test " + str(random.randint(0, 100)))
    project_description = ("Description_test " + str(random.randint(0, 100)))
    app.project.create_project(Project(name=project_name, description = project_description))
    print(Project)
    old_projects.append(Project(name=project_name, description = project_description))
    print("Appended _Old_projects: ", old_projects)
    new_projects = app.soap.get_project_list()
    print("New_projects: ", new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)