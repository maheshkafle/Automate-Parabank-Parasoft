from selenium.webdriver.common.by import By
import time
from Utils import XlUtil
from Utils.DateConverter import Date_split
from selenium.webdriver.support.ui import Select
from Utils.CustomLogger import Logsetup

class LoginPage:
    pass

    """Constructor"""
    def __init__(self, browser):
        self.browser = browser

    """ Locators """
    loginusername_name = "username"
    loginpassword_name = "password"
    clicklogin_xpath = "//input[@class='button']"
    logoutlink_xpath = "//*[@id='leftPanel']/ul/li[8]/a"
    linkopenaccount_xpath = "//a[contains(text(),'Open New Account')]"
    selectaccounttype_id = "type"
    accountoverview_xpath = "//a[contains(text(),'Accounts Overview')]"
    clickopenaccount_xpath = "//input[@class='button']"
    newaccountid_xpath = "//a[@id='newAccountId']"
    logger = Logsetup.getlogparabank()

    """Page Actions"""
    def login(self, username, password):
        self.browser.find_element(By.NAME, self.loginusername_name).send_keys(username)
        self.browser.find_element(By.NAME, self.loginpassword_name).send_keys(password)
        self.browser.find_element(By.XPATH, self.clicklogin_xpath).click()
        msg = "ParaBank | Accounts Overview"
        title = self.browser.title
        self.logger.info("-----Title----- %s" % (title))
        if msg == title:
            self.logger.info("Login Successful")
            return True
        else:
            self.logger.info("Login Successful")
            return False

    def accountcreation(self,type,filename):
        newaccountnumber = 00000
        self.browser.find_element_by_xpath(self.linkopenaccount_xpath).click()
        time.sleep(3)
        select = Select(self.browser.find_element_by_id(self.selectaccounttype_id))
        if type == "checking":
            select.select_by_visible_text("CHECKING")
        elif type == "savings":
            select.select_by_visible_text("SAVINGS")
        rows = XlUtil.getrowcount(filename,"Sheet1")
        columns = XlUtil.getcolumnount(filename,"Sheet1")
        for row in range(2,rows):
            Amount = XlUtil.readfromxl(filename,"Sheet1",row,2)
            accountnumber = XlUtil.readfromxl(filename,"Sheet1",row,1)
            amount =float(str.replace(Amount,'$',''))
            if amount >= 200:
                select = Select(self.browser.find_element_by_id(self.fromaccount_id))
                select.select_by_visible_text(accountnumber)
                self.browser.find_element_by_xpath(self.clickopenaccount_xpath).click()
                time.sleep(3)
                newaccountnumber = self.browser.find_element_by_xpath(self.newaccountid_xpath).text
                break
            else:
                newaccountnumber = 00000
                continue
        return newaccountnumber

    def accountoverview(self):
        self.browser.find_element_by_xpath(self.accountoverview_xpath).click()
        date1 = Date_split.datetimeconverter(self)
        filename = "C:\\Commit Projects\\Automate-Parabank-Parasoft\\Data" + date1 + ".xlsx"
        XlUtil.filecreate(filename)
        column = len(self.browser.find_elements_by_xpath("//table[@id='accountTable']//thead/tr/th"))
        row = len(self.browser.find_elements_by_xpath("//*[@id='accountTable']/tbody/tr"))
        for column in range(1, column + 1):
            data = self.browser.find_element_by_xpath(
                "//table[@id='accountTable']//thead/tr/th[" + str(column) + "]").text
            XlUtil.writetoxl(filename, "Sheet1", 1, column, data)
        for row in range(1, row + 1):
            for column in range(1, column + 1):
                data1 = self.browser.find_element_by_xpath(
                    "//table[@id='accountTable']//tbody//tr[" + str(row) + "]//td[" + str(column) + "]").text
                XlUtil.writetoxl(filename, "Sheet1", row + 1, column, data1)
        self.logger.info("Accounts Overview written to xls file")
        return filename

    def logout(self):
        self.browser.find_element(By.XPATH, self.logoutlink_xpath).click()
        self.logger.info("Logout Sucessful")
        time.sleep(3)
        self.logger.info("Closing browser")
        self.browser.close()