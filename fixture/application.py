from selenium import webdriver
from fixture.session import Session_helper
from fixture.project import Project_helper



class Application:

    def __init__(self, browser, base_url, project_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        #self.wd.implicitly_wait(60)
        self.session = Session_helper(self)
        self.base_url = base_url
        self.project_url = project_url
        self.project = Project_helper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()
