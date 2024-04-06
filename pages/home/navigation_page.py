import utilities.custom_logger as cl
import logging
from base.base_page import BasePage

class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super(NavigationPage, self).__init__(driver)
        self.driver = driver

    # Locators
    _logo = "//a/img[@class='img-fluid']"
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _interview = "INTERVIEW"
    _support = "SUPPORT"
    _blog = "BLOG"
    _practice = "PRACTICE"
    _my_courses = "MY COURSES"
    _community = "COMMUNITY"
    _noti_icon = "//a/i[@class='zc-icon-bell notification-bell']"
    _user_icon = "//button[@id='dropdownMenu1']"

    def navToHome(self):
        self.elementClick(self._home, locator_type="linktext")

    def navToAllCourses(self):
        self.elementClick(self._all_courses, locator_type="linktext")

    def navToInterview(self):
        self.elementClick(self._interview, locator_type="linktext")

    def navToSupport(self):
        self.elementClick(self._support, locator_type="linktext")

    def navToBlog(self):
        self.elementClick(self._blog, locator_type="linktext")

    def navToPractice(self):
        self.elementClick(self._practice, locator_type="linktext")

    def navToMyCourses(self):
        self.elementClick(self._my_courses, locator_type="linktext")

    def navToCommunity(self):
        self.elementClick(self._community, locator_type="linktext")

    def navToLogo(self):
        self.elementClick(self._logo, locator_type="xpath")

    def navToNotification(self):
        self.elementClick(self._noti_icon, locator_type="xpath")

    def navToUserSettings(self):
        self.elementClick(self._user_icon, locator_type="xpath")
