import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.ClearDatabase import ClearDatabasePage
from Pages.RegisterUser import RegisterUser
from Pages.AccountsOverviewPage import AccountsOverviewPage
import time
import pytest
from Utils.CustomLogger import Logsetup

class Test_AccountsOverview(BaseTest):

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)

    def testaccountoverview(self,handle_browser):
        self.object_ref = LoginPage(self.browser)
        self.object_ref.login(self.username, self.password)
        self.accounts_obj_ref = AccountsOverviewPage(self.browser)
        filename = self.accounts_obj_ref.accountoverview()
        time.sleep(3)
        self.object_ref.logout()
        time.sleep(3)
        if os.path.exists(filename) == True:
            assert True
        else:
            assert False
