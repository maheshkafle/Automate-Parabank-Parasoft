import pytest
from Tests.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Config.config import TestData


class Test_HomePageTest(BaseTest):

    def test_open_new_account_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_open_new_account_link_visible()
        assert flag

    def test_accounts_overview_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_accounts_overview_link_visible()
        assert flag

    def test_transfer_funds_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_transfer_funds_link_visible()
        assert flag

    def test_bill_pay_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_bill_pay_link_visible()
        assert flag

    def test_find_transactions_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_find_transactions_link_visible()
        assert flag

    def test_request_loan_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_request_loan_link_visible()
        assert flag

    def test_log_out_link_visible(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = self.home_page.is_log_out_link_visible()
        assert flag
