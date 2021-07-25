import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.ClearDatabase import ClearDatabasePage
import time
import pytest
from Utils.CustomLogger import Logsetup

class Test_ClearDatabasePage(BaseTest):

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)

    def testcleardb(self, handle_browser):
        self.locator = ClearDatabasePage(self.browser)
        self.locator.adminpagelink()
        time.sleep(3)
        result = self.locator.cleardatabase()
        self.browser.close()
        if result == True:
            assert True
        else:
            assert False