from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup

class RegisterUser():
    pass

    """Constructor"""
    def __init__(self, browser):
        self.browser = browser

    """ Locators """
    registerlink_xpath = "//a[contains(text(),'Register')]"
    inputfirstname_name = "customer.firstName"
    inputlastname_name = "customer.lastName"
    inputaddress_name = "customer.address.street"
    inputcity_name = "customer.address.city"
    inputstate_name = "customer.address.state"
    inputzipcode_name = "customer.address.zipCode"
    inputphone_name = "customer.phoneNumber"
    inputssn_name = "customer.ssn"
    inputusername_name = "customer.username"
    inputpassword_name = "customer.password"
    inputpasswordconfirm_name = "repeatedPassword"
    clickregister_xpath = "//table[@class='form2']//input[@class='button']"
    loginusername_name = "username"
    loginpassword_name = "password"
    clicklogin_xpath = "//input[@class='button']"

    logger = Logsetup.getlogparabank()

    """Page Actions"""

    def registerpage(self):
        self.browser.find_element_by_xpath(self.registerlink_xpath).click()

    def fillfirsname(self, firstname):
        self.browser.find_element_by_name(self.inputfirstname_name).send_keys(firstname)

    def filllastname(self, lastname):
        self.browser.find_element_by_name(self.inputlastname_name).send_keys(lastname)

    def filladdress(self, address):
        self.browser.find_element_by_name(self.inputaddress_name).send_keys(address)

    def fillcity(self, city):
        self.browser.find_element_by_name(self.inputcity_name).send_keys(city)

    def fillstate(self, state):
        self.browser.find_element_by_name(self.inputstate_name).send_keys(state)

    def fillzipcode(self, zipcode):
        self.browser.find_element_by_name(self.inputzipcode_name).send_keys(zipcode)

    def fillphone(self, phonenumber):
        self.browser.find_element_by_name(self.inputphone_name).send_keys(phonenumber)

    def fillssn(self, ssn):
        self.browser.find_element_by_name(self.inputssn_name).send_keys(ssn)

    def fillusername(self, username):
        self.browser.find_element_by_name(self.inputusername_name).send_keys(username)

    def fillpassword(self, password):
        self.browser.find_element_by_name(self.inputpassword_name).send_keys(password)

    def fillpasswordagain(self, password):
        self.browser.find_element_by_name(self.inputpasswordconfirm_name).send_keys(password)

    def registersubmit(self):
        self.browser.find_element_by_xpath(self.clickregister_xpath).click()

