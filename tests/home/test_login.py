from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)  # make this fixture available to complete scope where it's present
    def objectSetup(self, oneTimeSetUp):  # add the fixture where values come in
        self.login_page = LoginPage(self.driver)
        self.test_status = TestStatus(self.driver)


    # need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # if assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login("test@email.com", "abcabc")
        result1 = self.login_page.verifyLoginSucessful()
        self.test_status.mark(result1, "Login was successful")
        result2 = self.login_page.verifyTitleLoginPage()
        self.test_status.markFinal("test_valid_login", result2, "Title verified")

    @pytest.mark.run(order=1)
    def test_invalid_login_email_password_empty(self):
        self.login_page.logout()
        self.login_page.login()
        result_email = self.login_page.verifyLoginFailed_emailEmpty()
        result_password = self.login_page.verifyLoginFailed_passwordEmpty()
        self.test_status.mark(result_email, "email empty verified")
        self.test_status.markFinal("test_invalid_login_email_password_empty", result_password, "password empty verified")



