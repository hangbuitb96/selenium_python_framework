from pages.all_courses.all_courses_page import AllCoursesPage
# from pages.after_login_page.after_login_page import AfterLoginPage
from pages.buy_page.buy_page import BuyPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.all_courses = AllCoursesPage(self.driver)
        # self.after_login = AfterLoginPage(self.driver)
        self.buy_page = BuyPage(self.driver)
        self.test_status = TestStatus(self.driver)
        self.navigation = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\PC\\Desktop\\letskodeit\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, cc_num, cc_exp, cc_cvv):
        # self.after_login.navToAllCourses()
        self.all_courses.enrollCourse(full_course_name=course_name)
        self.buy_page.buyByCard(num=cc_num, date=cc_exp, cvv=cc_cvv) # leave empty

        result = self.buy_page.verifyEnrollFailedEmpty()
        self.test_status.markFinal("test_invalidEnrollment", result, "card number empty verified")

        self.navigation.navToAllCourses()


