import pytest
import json
import os.path
from fixture.application import Application

# глобальная переменная для хранения фикстуры
fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        # путь к конфигурационному файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

# инициализатор фикстуры подключения к вэбдрайверу
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    web_config_login = load_config(request.config.getoption("--target"))["webadmin"]
    web_config_projects = load_config(request.config.getoption("--target"))["web_config_projects"]
    if fixture is None or not fixture.is_valid():
        fixture =Application(browser=browser, base_url=web_config["baseUrl"], project_url=web_config_projects["project_url"])
    fixture.session.ensure_login(username=web_config_login["username"], password=web_config_login["password"])
    return fixture


# фикстура выполнится несмотря на то, что нигде не указана
# благодаря параметру autouse
@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")










