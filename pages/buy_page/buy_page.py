import utilities.custom_logger as cl
import logging
from base.base_page import BasePage

class BuyPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super(BuyPage, self).__init__(driver)
        self.driver = driver

    _cc_num = "//input[@name='cardnumber']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _country = "//select[@name='country-list']"
    _buy_btn = "//div[@class='col-xs-12']/button[1]"
    _cookie = "//div[@id='cookie_box']/div[contains(text(),'X')]"
    _all_courses = "(//a[@href='/courses'])[1]"
    def enterCardNum(self, num):
        # self.switchToFrame(name="__privateStripeFrame0886")
        self.switchFrameByIndex(self._cc_num, "xpath")
        self.elementSendKeys(num, self._cc_num, "xpath")
        self.switchToDefaultContent()

    def enterCardExpiredDate(self, date):
        # self.switchToFrame(name="__privateStripeFrame08810")
        self.switchFrameByIndex(self._cc_exp, "xpath")
        self.elementSendKeys(date, self._cc_exp, "xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame0888")
        self.switchFrameByIndex(self._cc_cvv, "xpath")
        self.elementSendKeys(cvv, self._cc_cvv, "xpath")
        self.switchToDefaultContent()

    def selectCountry(self, country):
        self.elementSelectByVisibleText(country, self._country, "xpath")


    def enterCardInfo(self, num="", date="", cvv="", country=""):
        self.scrollElementIntoView(self._buy_btn, "xpath")
        self.enterCardNum(num)
        self.enterCardExpiredDate(date)
        self.enterCardCVV(cvv)
        self.selectCountry(country)

    def clickBuyBtn(self):
        buy_btn = self.waitToBeClickable(self._buy_btn, "xpath", 20)
        self.elementClick(element=buy_btn)

    def clickBuyBtnJS(self):
        self.jsElementClick(self._buy_btn, "xpath")

    def closeCookie(self):
        self.elementClick(self._cookie, "xpath")

    def buyByCard(self, num="", date="", cvv="", country=""):
        self.enterCardInfo(num, date, cvv, country)
        # self.closeCookie()
        # self.clickBuyBtn()
        self.clickBuyBtnJS()

    def verifyEnrollFailedEmpty(self):
        message = self.waitVisibility("//span[contains(text(), 'Your card number is incomplete.')]", "xpath")
        result = self.isElementDisplayed(element=message)
        return result

    def navToAllCourses(self):
        from pages.all_courses.all_courses_page import AllCoursesPage
        # self.webScroll(direction="up")
        self.elementClick(self._all_courses, "xpath")
        self.log.info("Navigate to All Courses")
        return AllCoursesPage(self.driver)
