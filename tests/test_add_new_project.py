

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    app.wd.find_element('xpath', "//input[@value='Create New Project']").click()
    app.project.create_project("New project-2", "This is my very second project")

    """group =json_groups
    #old_groups = db.get_group_list()
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""