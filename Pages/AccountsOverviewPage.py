from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup
from Utils.DateConverter import Date_split
from Utils import XlUtil

class AccountsOverviewPage:
    pass

    accountoverview_xpath = "//a[contains(text(),'Accounts Overview')]"
    logger = Logsetup.getlogparabank()
    
    """Constructor"""
    def __init__(self, browser):
        self.browser = browser


    def accountoverview(self):
        self.browser.find_element_by_xpath(self.accountoverview_xpath).click()
        time.sleep(5)
        # date1 = datetime.date.today()
        # date1 = Date_spilt.dateconverter(date1)
        # date1 =str(date1)
        date1= Date_spilt.datetimeconverter(self)
        filename="C:\\Commit Projects\\Automate-Parabank-Parasoft\\Data"+date1+".xlsx"
        XlUtil.filecreate(filename)
        # print (date1)
        # print (filename)
        column = len(self.browser.find_elements_by_xpath("//table[@id='accountTable']//thead/tr/th"))
        row = len(self.browser.find_elements_by_xpath("//*[@id='accountTable']/tbody/tr"))
        # print (coln,row)
        for column in range(1,column+1):
            data = self.browser.find_element_by_xpath("//table[@id='accountTable']//thead/tr/th["+str(column)+"]").text
            XlUtil.writetoxl(filename,"Sheet1",1,column,data)
        for row in range(1,row+1):
            for column in range(1,column+1):
                data1 = self.browser.find_element_by_xpath("//table[@id='accountTable']//tbody//tr["+str(row)+"]//td["+str(column)+"]").text
                XlUtil.writetoxl(filename,"Sheet1",row+1,column,data1)
        self.logger.info("Accounts Overview written to xls file")
        return filename