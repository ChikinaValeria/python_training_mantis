
from model.project import Project
import random

def test_delete_project(app):
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.create_project(Project(name="test_name", description = "test_description"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)