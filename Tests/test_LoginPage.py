import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
import time
import pytest
from Utils.CustomLogger import Logsetup

class TestLoginPage(BaseTest):

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)


    def testlogin(self, handle_browser):
        self.locator = LoginPage(self.browser)
        result = self.locator.login(self.username,self.password)
        time.sleep(3)
        self.locator.logout()
        if result == True:
            assert True
        else:
            assert False