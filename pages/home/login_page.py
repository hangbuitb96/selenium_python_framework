import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locator_type="xpath")

    def enterEmail(self, email):
        self.elementSendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.elementSendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSucessful(self):
        result = self.isElementPresent("//h1[contains(text(),'My Courses')]",
                                       locator_type="xpath")
        return result

    def verifyLoginFailed_emailEmpty(self):
        result = self.isElementPresent("//span[contains(text(), 'The email field is required')]",
                                       locator_type="xpath")
        return result

    def verifyLoginFailed_passwordEmpty(self):
        result = self.isElementPresent("//span[contains(text(), 'The password field is required.')]",
                                       locator_type="xpath")
        return result

    def verifyLoginFailed_invalidEmail(self):
        result = self.isElementPresent("//span[contains(text(), 'The email must be a valid email address.')]",
                                       locator_type="xpath")
        return result

    def verifyLoginFailed_invalidDetails(self):
        result = self.isElementPresent("incorrectdetails") # locator_type = "id"
        return result

    def verifyTitleLoginPage(self):
        title = self.waitForTitleContains("My Courses")
        return title

    def logout(self):
        self.nav.navToUserSettings()
        self.elementClick(locator="//a[@href='/logout']", locator_type="xpath")