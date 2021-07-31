import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.AccountsOverviewPage import AccountsOverviewPage
from Pages.TransferAccount import TransferAccount
from Utils.DateConverter import Date_split
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

    def testamounttransfer(self,handle_browser):
        self.ref_obj = LoginPage(self.browser)
        self.ref_obj.login(self.username,self.password)
        self.accounts_obj_ref = AccountsOverviewPage(self.browser)
        filename = self.accounts_obj_ref.accountoverview()
        time.sleep(3)
        self.ref_obj = TransferAccount(self.browser)
        result = self.ref_obj.transferaccount(filename)
        time.sleep(3)
        self.ref_obj = LoginPage(self.browser)
        self.ref_obj.logout()
        if result == True:
            assert True
            self.logger.info("Account transfer successful")
        else:
            self.logger.info("Account transfer not successful")
            assert False