import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from pages.buy_page.buy_page import BuyPage
class AllCoursesPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super(AllCoursesPage, self).__init__(driver)
        self.driver = driver

    _search_box = "//input[@id='search']"
    _search_btn = "//button[@type='submit']"
    _course = "//div[@id='course-list']//h4[contains(text(),'{0}')]"
    _enroll_btn = "//button[contains(text(), 'Enroll in Course')]"

    def searchCourseName(self, name):
        el_search_box = self.waitToBeClickable(self._search_box, "xpath")
        self.elementSendKeys(name, element=el_search_box)
        self.elementClick(self._search_btn)

    def selectCourse(self, full_course_name):
        self.elementClick(locator=self._course.format(full_course_name), locator_type="xpath")

    def clickEnroll(self):
        el_enroll_btn = self.waitToBeClickable(locator=self._enroll_btn, locator_type="xpath")
        self.elementClick(element=el_enroll_btn)

    def enrollCourse(self, full_course_name):
        self.selectCourse(full_course_name)
        self.clickEnroll()
        return BuyPage(self.driver)
