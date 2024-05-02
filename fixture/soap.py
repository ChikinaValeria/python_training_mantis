from suds.client import Client
from suds import WebFault
from fixture.project import Project
class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.soapUrl)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.soapUrl)
        list = []
        username = self.app.username
        password = self.app.password

        try:
            body = client.service.mc_projects_get_user_accessible(username, password)
            if len(body) > 0:
                for i in range(len(body)):
                    id = body[i].id
                    name = body[i].name
                    description = body[i].description
                    list.append(Project(id=id,
                                        name=name,
                                        description=description))
                return list
            else:
                return list
        except WebFault:
            print("Ошибка!")
            return False



