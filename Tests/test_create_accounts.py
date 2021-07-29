import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Utils import XlUtil
from Utils.DateConverter import Date_split
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.AccountsOverviewPage import AccountsOverviewPage
from Pages.RegisterUser import RegisterUser
from selenium.webdriver.support.ui import Select
import time
import pytest
from Utils.CustomLogger import Logsetup


class TestCreateAccounts(BaseTest):
    logger = Logsetup.getlogparabank()

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)

    def testcheckingaccont(self, handle_browser):

        mark = 'not found'
        self.ref_obj = LoginPage(self.browser)
        self.ref_obj.login(self.username, self.password)
        filename = self.ref_obj.accountoverview()
        time.sleep(3)
        newaccount = self.ref_obj.accountcreation("checking", filename)
        filename = self.ref_obj.accountoverview()
        time.sleep(3)
        self.ref_obj.logout()
        rows = XlUtil.getrowcount(filename, "Sheet1")
        for row in range(2, rows):
            accountnumber = XlUtil.readfromxl(filename, "Sheet1", row, 1)
            # print(accountnumber, newaccount)
            if newaccount == accountnumber:
                mark = "success"
                break
            else:
                mark = "not found"
                continue
        if mark == "success":
            print("Checking account- ", newaccount, " created sucessfully")
            self.logger.info("Checking account created")
            assert True
        else:
            print("failure to create a new account")
            self.logger("Checking account not created")
            assert False
    
    