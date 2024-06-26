import re
import time
class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "/signup_page.php")
        wd.find_element('name', "username").send_keys(username)
        time.sleep(2)
        wd.find_element('name', "email").send_keys(email)
        time.sleep(2)
        wd.find_element('xpath', "//input[@value='Signup']").click()


        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        wd.get(url)
        wd.find_element('name', "password").send_keys(password)
        time.sleep(2)
        wd.find_element('name', "password_confirm").send_keys(password)
        time.sleep(2)
        wd.find_element('xpath', "//input[@value='Update User']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)