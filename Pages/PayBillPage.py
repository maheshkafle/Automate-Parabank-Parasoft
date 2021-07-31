from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup
from Utils.DateConverter import Date_split
from selenium.webdriver.support.ui import Select
from Utils import XlUtil


class PayBillPage:
    pass

    linkbillpay_xpath = "//a[contains(text(),'Bill Pay')]"
    fillpayeename_name = "payee.name"
    fillpayeeaddress_name = "payee.address.street"
    fillpayeecity_name = "payee.address.city"
    fillpyeestate_name = "payee.address.state"
    fillpayeezip_name = "payee.address.zipCode"
    fillpayeestate_name = "payee.address.state"
    fillpayeeph_name = "payee.phoneNumber"
    fillpayeeaccount_name = "payee.accountNumber"
    fillpayeeverify_name = "verifyAccount"
    sendpayment_xpath = "//input[@class='button']"
    fillpayeeamount_name = "amount"
    selectfromaccountpayee_xpath = "//select[@name='fromAccountId']"
    logger = Logsetup.getlogparabank()

    """Constructor"""

    def __init__(self, browser):
        self.browser = browser


    def clickpaybill(self):
        self.browser.find_element_by_xpath(self.linkbillpay_xpath).click()
    def inputpayeename(self ,payeename):
        self.browser.find_element_by_name(self.fillpayeename_name).send_keys(payeename)
    def inputpayeeaddres(self ,payeeaddress):
        self.browser.find_element_by_name(self.fillpayeeaddress_name).send_keys(payeeaddress)
    def inputpayeecity(self ,payeecity):
        self.browser.find_element_by_name(self.fillpayeecity_name).send_keys(payeecity)
    def inputpayeestate(self ,payeestate):
        self.browser.find_element_by_name(self.fillpayeestate_name).send_keys(payeestate)
    def inputpayeezipcode(self ,payeezip):
        self.browser.find_element_by_name(self.fillpayeezip_name).send_keys(payeezip)
    def inputpayeeph(self ,payeeph):
        self.browser.find_element_by_name(self.fillpayeeph_name).send_keys(payeeph)
    def inputpayeeaccount(self ,payeeaccount):
        self.browser.find_element_by_name(self.fillpayeeaccount_name).send_keys(payeeaccount)
    def inputpayeeverify(self ,payeeaccount):
        self.browser.find_element_by_name(self.fillpayeeverify_name).send_keys(payeeaccount)
    def clickpaymentbutton(self):
        self.browser.find_element_by_xpath(self.sendpayment_xpath).click()
    def inputpayeeamount(self ,amount):
        self.browser.find_element_by_name(self.fillpayeeamount_name).send_keys(amount)
    def selectbillpayaccount(self ,accountnumber):
        select = Select(self.browser.find_element_by_xpath(self.selectfromaccountpayee_xpath))
        select.select_by_visible_text(str(15342))
