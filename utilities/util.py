"""
@package util

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):
    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info = ""):
        """
        put the program to wait for the specific amount of time
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        """
        Get random string of characters
        Parameters:
             length: length of string, number of characters string should have
             type: type of characters string should have. Default is letters
             Provide lower/upper/digits for different types
        """
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, char_count=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(char_count, "lower")

    def getUniqueNameList(self, list_size=5, item_length=None):
        """
        Get a list of unique names
        Parameters:
            list_size: number of names. Default is 5 names in a list
            item_length: it should be a list containing number of items equal to the list_size
                        this determines the length of each item in the list
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.getUniqueName(item_length[i]))
        return name_list

    def verifyTextContains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        Parameters:
            expected_text
            actual_text
        """
        self.log.info("Actual text from application web UI --> :: " + actual_text)
        self.log.info("Expected text from application web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS!!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAIN!!!")
            return False

    def verifyTextMatch(self, actual_text, expected_text):
        """
        Verify actual text matches expected text string
        Parameters:
            expected_text
            actual_text
        """
        self.log.info("Actual text from application web UI --> :: " + actual_text)
        self.log.info("Expected text from application web UI --> :: " + expected_text)
        if expected_text.lower() == actual_text.lower():
            self.log.info("### VERIFICATION MATCHES!!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH!!!")
            return False

    def verifyListMatch(self, expected_list, actual_list):
        """
        Verify two list matches
        :param expected_list:
        :param actual_list:
        """
        return set(expected_list) == set(actual_list)

    def verifyListContains(self, expected_list, actual_list):
        """
        Verify actual list contains items of expected list
        :param expected_list:
        :param actual_list:
        """
        length = len(expected_list)
        for i in range(0,length):
            if expected_list[i] not in actual_list:
                return False
            else:
                return True
