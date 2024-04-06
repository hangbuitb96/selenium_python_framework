"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

example:
   wdf = WebDriverFactory(browser)
   wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os

class WebDriverFactory():
    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        Returns:
            None
        """
        self.browser = browser
    """
        Set Chrome driver and Edge environment based on OS
        chromedriver = "C:/.../chromedriver.exe
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        baseUrl = "https://www.letskodeit.com/"
        if self.browser == "edge":
            # Set Ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            # chromedriver = "C:\\Users\\PC\\WebDriver\\bin\\chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome()
            # driver.set_window_size(1920, 1080)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for an Element
        driver.implicitly_wait(10)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with app URL
        driver.get(baseUrl)
        return driver
