from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class HomePage(BasePage):

    """By locators or Object Repositories"""
    OPEN_NEW_ACCOUNT_LINK = (By.LINK_TEXT, 'Open New Account')
    ACCOUNTS_OVERVIEW_LINK = (By.LINK_TEXT,'Accounts Overview')
    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, 'Transfer Funds')
    BILL_PAY_LINK = (By.LINK_TEXT, 'Transfer Funds')
    FIND_TRANSACTIONS_LINK = (By.LINK_TEXT, 'Find Transactions')
    REQUEST_LOAN_LINK = (By.LINK_TEXT, 'Request Loan')
    LOG_OUT_LINK = (By.LINK_TEXT, 'Log Out')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)


    """Page Actions"""

    """Used to get home page title"""
    def is_open_new_account_link_visible(self):
        flag = self.is_visible(self.OPEN_NEW_ACCOUNT_LINK)
        return flag

    def is_accounts_overview_link_visible(self):
        flag = self.is_visible(self.ACCOUNTS_OVERVIEW_LINK)
        return flag

    def is_transfer_funds_link_visible(self):
        flag = self.is_visible(self.TRANSFER_FUNDS_LINK)
        return flag

    def is_bill_pay_link_visible(self):
        flag = self.is_visible(self.BILL_PAY_LINK)
        return flag

    def is_find_transactions_link_visible(self):
        flag = self.is_visible(self.FIND_TRANSACTIONS_LINK)
        return flag

    def is_request_loan_link_visible(self):
        flag = self.is_visible(self.REQUEST_LOAN_LINK)
        return flag

    def is_log_out_link_visible(self):
        flag = self.is_visible(self.LOG_OUT_LINK)
        return flag

    # """Used to validate if sign_up link exits"""
    # def get_accounts_overview_link(self):
    #     return self.do_click(self.ACCOUNTS_OVERVIEW_LINK)

    # """Used to login to App and Assert Welcome Message after login is successful"""
    # def do_login(self, username, password):
    #     self.do_send_keys(self.EMAIL, username)
    #     self.do_send_keys(self.PASSWORD, password)
    #     self.do_click(self.LOGIN_BUTTON)
    #     self.driver.implicitly_wait(10)
    #     WELCOME_MSG = self.get_element_text(self.XPATH_WELCOME_MSG)
    #     assert WELCOME_MSG