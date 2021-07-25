from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup

class LoginPage:
    pass

    """Constructor"""

    """Page Actions"""

    def __init__(self, browser):
        self.browser = browser

    loginusername_name = "username"
    loginpassword_name = "password"
    clicklogin_xpath = "//input[@class='button']"
    logoutlink_xpath = "//*[@id='leftPanel']/ul/li[8]/a"
    logger = Logsetup.getlogparabank()

    def login(self, username, password):
        self.browser.find_element(By.NAME, self.loginusername_name).send_keys(username)
        self.browser.find_element(By.NAME, self.loginpassword_name).send_keys(password)
        self.browser.find_element(By.XPATH, self.clicklogin_xpath).click()
        msg = "ParaBank | Accounts Overview"
        title = self.browser.title
        print("title--------------", title)
        if msg == title:
            self.logger.info("Login Sucessful")
            return True
        else:
            self.logger.info("Login Sucessful")
            return False


    def logout(self):
        self.browser.find_element(By.XPATH, self.logoutlink_xpath).click()
        self.logger.info("Logout Sucessful")
        time.sleep(3)
        self.logger.info("Closing browser")
        self.browser.close()