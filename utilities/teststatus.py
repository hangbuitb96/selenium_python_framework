"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack

class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits Check Point class
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def setResult(self, result, result_message):
        try:
            if result is not None:
                if result: # if result is True
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.info("### VERIFICATION FAIL :: + " + result_message)
                    self.screenShot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAIL :: + " + result_message)
                self.screenShot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception occurred!!!")
            self.screenShot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, result_message)

    def markFinal(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True
