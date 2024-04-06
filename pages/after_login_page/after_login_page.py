import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from pages.all_courses.all_courses_page import AllCoursesPage

class AfterLoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    _block = "//div[@class='blockUI blockOverlay']"
    _all_courses = "(//a[@href='/courses'])[1]"

    def __init__(self, driver):
        super(AfterLoginPage, self).__init__(driver)
        self.driver = driver

    def navToAllCourses(self):
        self.waitInvisibility(self._block, "xpath", 20)
        self.elementClick(self._all_courses, "xpath")
        self.log.info("Navigate to All Courses")
        return AllCoursesPage(self.driver)
