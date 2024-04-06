from selenium.webdriver.common.by import By
from traceback import print_stack
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "_" + str(round(time.time()*1000)) + ".png"
        screenshot_directory = "..\\screenshots\\"
        relative_file_name = screenshot_directory + file_name # ../screenshots/[file_name].png
        current_directory = os.path.dirname(__file__) # C:/path.../base
        destination_file = os.path.join(current_directory, relative_file_name) # C:/path.../base/../screenshots/[file_name].png
        destination_directory = os.path.join(current_directory, screenshot_directory) # # C:/path.../base/../screenshots
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("### Exception occurred")
            print_stack()
    def getTitle(self):
        return self.driver.title

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type" + locator_type + "is NOT correct/supported")
        return False

    def getElement(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element FOUND with locator: " + locator
                            + "locator type: " + locator_type)
        except:
            self.log.info("Element NOT FOUND with locator: " + locator
                            + "locator type: " + locator_type)
        return element

    def getElementList(self, locator, locator_type='id'):

        locator_type = locator_type.lower()
        by_type = self.getByType(locator_type)
        elements = self.driver.find_elements(by_type, locator)
        if len(elements) > 0:
            self.log.info("Element List FOUND with locator: " + locator
                            + "locator type: " + locator_type)
        else:
            self.log.info("Element list NOT FOUND with locator: " + locator
                            + "locator type: " + locator_type)
        return elements

    def elementClick(self, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator: # if locator is NOT empty
                element = self.getElement(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + "locator type: " + locator_type)
        except:
            self.log.info("CANNOT click on element with locator: " + locator + "locator type: " + locator_type)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def jsElementClick(self, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator: # if locator is NOT empty
                element = self.getElement(locator, locator_type)
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info("Hard-Clicked on element with locator: " + locator + "locator type: " + locator_type)
        except:
            self.log.info("Cannot click on element with locator: " + locator + "locator type: " + locator_type)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def elementSendKeys(self, data, locator="", locator_type="id", element=None):
        try:
            if locator: # if locator is NOT empty
                element = self.getElement(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator
                            + "locator type: " + locator_type)
        except:
            self.log.info("CANNOT send data on element with locator: " + locator
                            + "locator type: " + locator_type)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def sendKeysWhenReady(self, data, locator="", locator_type="id"):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            by_type = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(10) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=10,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def clearField(self, locator="", locator_type="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locator_type)

    def elementSelectByVisibleText(self, text, locator="", locator_type="id", element=None):
        try:
            if locator: # if locator is NOT empty
                element = self.getElement(locator, locator_type)
            sel = Select(element)
            sel.select_by_visible_text(text)
            self.log.info("Select " + text + "with locator: " + locator
                            + "locator type: " + locator_type)
        except:
            self.log.info("Cannot select " + text + "with locator: " + locator
                            + "locator type: " + locator_type)
            print_stack()

    def getText(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator: # if locator is NOT empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip() # remove spaces at the beginning and at the end of the string
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locator_type="id"):
        try:
            if locator:
                element_list = self.getElementList(locator, locator_type)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + locator_type)
                return True
            else:
                self.log.info("Element NOT present with locator: " + locator +
                              " locator_type: " + locator_type)
                return False
        except:
            self.log.info("Element NOT found")
            return False

    def isElementDisplayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        is_displayed = False
        try:
            if locator:
                element = self.getElement(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locator_type: " + locator_type)
            else:
                self.log.info("Element is NOT displayed with locator: " + locator +
                              " locator_type: " + locator_type)
            return is_displayed
        except:
            self.log.info("Element NOT found")
            return False

    def elementPresenceCheck(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element NOT present with locator: " + locator +
                              " locatorType: " + str(by_type))
                return False
        except:
            self.log.info("Element NOT found")
            return False

    def waitVisibility(self, locator="", locator_type="id",
                       timeout=20, poll_frequency=0.5):

        element = None
        try:
            by_type = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located(
                (by_type, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element NOT appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))
        return element

    def waitInvisibility(self, locator="", locator_type="id",
                       timeout=20, poll_frequency=0.5):
        element = None
        try:
            by_type = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be invisible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.invisibility_of_element(
                (by_type, locator)))

            self.log.info("Element disappeared on the web page")

        except:
            self.log.info("Element STILL appears on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))
        return element


    def waitForPresence(self, locator="", locator_type="id",
                       timeout=20, poll_frequency=0.5):

        element = None
        try:
            by_type = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be present")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.presence_of_element_located(
                (by_type, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

        return element

    def waitForTitleContains(self, title,
                       timeout=20, poll_frequency=0.5):

        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for title to be present")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.title_contains(title))

            self.log.info("Title appeared on the web page")

        except:
            self.log.info("Title not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

        return element


    def waitToBeClickable(self, locator="", locator_type="id",
                       timeout=20, poll_frequency=0.5):

        element = None
        try:
            by_type = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(
                (by_type, locator)))
            self.log.info("Element clickable on the web page")

        except:
            self.log.info("Element not clickable on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def scrollElementIntoView(self, locator, locator_type = "id", element=None):
        try:
            if locator:  # if locator is NOT empty
                element = self.getElement(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info("Scrolled element into view with locator: " + locator + "locator type: " + locator_type)
        except:
            self.log.info("CANNOT FIND element with locator: " + locator + "locator type: " + locator_type)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def switchFrameByIndex(self, locator, locator_type="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", "xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locator_type)
                # if the element is present, break out of the loop
                # else, switch to default content then go to the next frame
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            self.log.info("iFrame index NOT found")
            return result

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe
        Parameters:
            1. Required:
                None
            2. Optional:
                1.id - id of the iframe
                2.name - name of the iframe
                3.index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locator_type="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value


    def isEnabled(self, locator, locator_type="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locator_type=locator_type)
        enabled = False
        try:
            attribute_value = self.getElementAttributeValue(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled
