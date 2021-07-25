from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup

class ClearDatabasePage:
    pass

    """Constructor"""
    def __init__(self, browser):
        self.browser = browser

    """ Locators """
    adminpagelink_xpath = "//a[contains(text(),'Admin Page')]"
    dbclean_xpath = "//button[contains(text(),'Clean')]"
    logger = Logsetup.getlogparabank()

    """Page Actions"""
    def adminpagelink(self):
        self.browser.find_element_by_xpath(self.adminpagelink_xpath).click()

    def cleardatabase(self):
        msg = "Database Cleaned"
        self.browser.find_element_by_xpath(self.dbclean_xpath).click()
        bodytext = self.browser.find_element_by_tag_name("Body").text
        if msg in bodytext:
            self.logger.info("Database cleaned")
            return True
        else:
            self.logger.info("Database not cleaned")
            return False
