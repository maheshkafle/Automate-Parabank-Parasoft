import os.path
from selenium import webdriver
from Utils.readconfigfile import Getinfoconfig
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.ClearDatabase import ClearDatabasePage
from Pages.RegisterUser import RegisterUser
import time
import pytest
from Utils.CustomLogger import Logsetup

class Test_registeruser(BaseTest):

    @pytest.fixture()
    def handle_browser(self, init_driver):
        self.browser = init_driver
        self.browser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.browser.maximize_window()
        self.locator = LoginPage(self.browser)

    def testregister(self, handle_browser):
        self.register_user_obj = RegisterUser(self.browser)
        self.register_user_obj.registerpage()
        time.sleep(5)
        self.register_user_obj.fillfirsname(self.firstname)
        self.register_user_obj.filllastname(self.lastname)
        self.register_user_obj.filladdress(self.address)
        self.register_user_obj.fillcity(self.city)
        self.register_user_obj.fillstate(self.state)
        self.register_user_obj.fillzipcode(self.zipcode)
        self.register_user_obj.fillphone(self.phonenumber)
        self.register_user_obj.fillssn(self.ssn)
        self.register_user_obj.fillusername(self.username)
        self.register_user_obj.fillpassword(self.password)
        self.register_user_obj.fillpasswordagain(self.password)
        self.register_user_obj.registersubmit()
        title = self.browser.title
        time.sleep(3)
        self.LoginPage = LoginPage(self.browser)
        self.LoginPage.logout()
        Act_title = "ParaBank | Customer Created"
        if Act_title == title:
            assert True
        else:
            assert False