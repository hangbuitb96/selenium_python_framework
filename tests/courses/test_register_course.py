from pages.all_courses.all_courses_page import AllCoursesPage
from pages.after_login_page.after_login_page import AfterLoginPage
from pages.buy_page.buy_page import BuyPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.all_courses = AllCoursesPage(self.driver)
        self.after_login = AfterLoginPage(self.driver)
        self.buy_page = BuyPage(self.driver)
        self.test_status = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.after_login.navToAllCourses()
        self.all_courses.enrollCourse(name="javascript")
        self.buy_page.buyByCard() # leave empty

        result = self.buy_page.verifyEnrollFailedEmpty()
        self.test_status.markFinal("test_invalidEnrollment", result, "card number empty verified")


