import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Pages.PayBillPage import PayBillPage
from Tests.test_Base import BaseTest
from Pages.AccountsOverviewPage import AccountsOverviewPage
from Utils import XlUtil
import time
import pytest
from Utils.CustomLogger import Logsetup

class TestPayBills(BaseTest):

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)

    def testpaybill(self, handle_browser):
        self.ref_obj = LoginPage(self.browser)
        self.ref_obj.login(self.username, self.password)
        filename = self.ref_obj.accountoverview()
        time.sleep(3)
        self.ref_obj = PayBillPage(self.browser)
        self.ref_obj.clickpaybill()
        time.sleep(3)
        self.ref_obj.inputpayeename(self.payeename)
        self.ref_obj.inputpayeeaddres(self.payeeaddress)
        self.ref_obj.inputpayeecity(self.payeecity)
        self.ref_obj.inputpayeestate(self.payeestate)
        self.ref_obj.inputpayeezipcode(self.payeezip)
        self.ref_obj.inputpayeeph(self.payeeph)
        self.ref_obj.inputpayeeaccount(self.payeeaccount)
        self.ref_obj.inputpayeeverify(self.payeeaccount)
        self.ref_obj.inputpayeeamount(self.amount)
        time.sleep(3)
        accountnumber = XlUtil.readfromxl(filename, "Sheet1", 2, 1)
        self.ref_obj.selectbillpayaccount(accountnumber)
        time.sleep(3)
        self.ref_obj.clickpaymentbutton()
        time.sleep(3)
        msg = self.browser.find_element_by_xpath("//h1[contains(text(),'Bill Payment Complete')]").text
        time.sleep(3)
        self.ref_obj = LoginPage(self.browser)
        self.ref_obj.logout()
        if msg == "Bill Payment Complete":
            self.logger.info("Bill pay sucessful")
            print("Bill Payment to ", self.payeename, "in the amount of ", self.amount, "from account ", accountnumber,
                  " was successful.")
            assert True
        else:
            print("Payment failure")
            self.logger.info("Bill payment failed")
            assert False
