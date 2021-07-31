from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup
from Utils.DateConverter import Date_split
from selenium.webdriver.support.ui import Select
from Utils import XlUtil

class TransferAccount:
    pass

    inputtransferamount = "//input[@id='amount']"
    selectfromaccount_xpath = "//select[@id='fromAccountId']"
    selecttoaccount_xpath = "//select[@id='toAccountId']"
    linktransfer_xpath = "//a[contains(text(),'Transfer Funds')]"
    clicktransferbutton = "//input[@class='button']"
    logger = Logsetup.getlogparabank()

    """Constructor"""
    def __init__(self, browser):
        self.browser = browser


    def transferaccount(self ,filename):
        self.browser.find_element_by_xpath(self.linktransfer_xpath).click()
        time.sleep(3)
        rows = XlUtil.getrowcount(filename ,"Sheet1")
        columns = XlUtil.getcolumnount(filename ,"Sheet1")
        sourceaccount = XlUtil.readfromxl(filename ,"Sheet1" ,2 ,1)
        sourceamount = XlUtil.readfromxl(filename ,"Sheet1" ,2 ,2)
        sourceamount1 = float(str.replace(sourceamount, '$', ''))
        targetaccount = XlUtil.readfromxl(filename ,"Sheet1" ,3 ,1)
        targetaccountamount = XlUtil.readfromxl(filename ,"Sheet1" ,3 ,2)
        targetaccountamount1 = float(str.replace(targetaccountamount ,'$' ,''))
        if sourceamount1 >200:
            self.browser.find_element_by_xpath(self.inputtransferamount).send_keys("100")
            select = Select(self.browser.find_element_by_xpath(self.selectfromaccount_xpath))
            select.select_by_visible_text(sourceaccount)
            select = Select(self.browser.find_element_by_xpath(self.selecttoaccount_xpath))
            select.select_by_visible_text(targetaccount)
            self.browser.find_element_by_xpath(self.clicktransferbutton).click()
            time.sleep(3)
            msg = self.browser.find_element_by_xpath("//*[@id='rightPanel']/div/div/h1").text
            if msg == "Transfer Complete!":
                print("$100 transferred from ", sourceaccount, " to ", targetaccount)
                self.logger.info("100 transferred")
                return True
            else:
                print("Transfer failed")
                self.logger.info("transfer failed")
                return False
        else:
            print("Insufficent balance")
            self.logger.info("Insufficent funds")
            return False