import pytest
import json
import os.path
from fixture.application import Application
import ftputil
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
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    web_config_login = load_config(request.config.getoption("--target"))["webadmin"]
    if fixture is None or not fixture.is_valid():
        fixture =Application(browser=browser, config=config)
    fixture.session.ensure_login(username=web_config_login["username"], password=web_config_login["password"])
    return fixture


@pytest.fixture(scope = "session")
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture(scope = "session", autouse = True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)


def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc1.php"):
            remote.remove("config_inc1.php")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc1.php")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc1.php"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc1.php", "config_inc.php")

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










