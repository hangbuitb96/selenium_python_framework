import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from pages.after_login_page.after_login_page import AfterLoginPage
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="class") # means that this fixture applied to this scope
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lg = LoginPage(driver)
    after_login = AfterLoginPage(driver)
    lg.login("test@email.com", "abcabc")
    after_login.navToAllCourses()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help = "Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")