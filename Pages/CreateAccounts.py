from selenium.webdriver.common.by import By
import time
from Utils.CustomLogger import Logsetup
from Utils.DateConverter import Date_split
from selenium.webdriver.support.ui import Select
from Utils import XlUtil


class CreateAccountsPage:
    pass

    accountoverview_xpath = "//a[contains(text(),'Accounts Overview')]"
    linkopenaccount_xpath = "//a[contains(text(),'Open New Account')]"
    selectaccounttype_id = "type"
    fromaccount_id = "fromAccountId"
    clickopenaccount_xpath = "//input[@class='button']"
    newaccountid_xpath = "//a[@id='newAccountId']"
    logger = Logsetup.getlogparabank()

    """Constructor"""

    def __init__(self, browser):
        self.browser = browser

# def accountoverview(self):
#     self.browser.find_element_by_xpath(self.accountoverview_xpath).click()
#     date1 = Date_split.datetimeconverter(self)
#     filename = "C:\\Commit Projects\\parabank-testing\\data" + date1 + ".xlsx"
#     XlUtil.filecreate(filename)
#     coln = len(self.browser.find_elements_by_xpath("//table[@id='accountTable']//thead/tr/th"))
#     row = len(self.browser.find_elements_by_xpath("//*[@id='accountTable']/tbody/tr"))
#     for c in range(1, coln + 1):
#         data = self.browser.find_element_by_xpath("//table[@id='accountTable']//thead/tr/th[" + str(c) + "]").text
#         XlUtil.writetoxl(filename, "Sheet1", 1, c, data)
#     for r in range(1, row + 1):
#         for c in range(1, coln + 1):
#             data1 = self.Openbrowser.find_element_by_xpath(
#                 "//table[@id='accountTable']//tbody//tr[" + str(r) + "]//td[" + str(c) + "]").text
#             XlUtil.writetoxl(filename, "Sheet1", r + 1, c, data1)
#     self.logger.info("account overview written to xls file")
#     return filename

# def accountcreation(self,type,filename):
#     self.browser.find_element_by_xpath(self.linkopenaccount_xpath).click()
#     time.sleep(3)
#     select = Select(self.browser.find_element_by_id(self.selectaccounttype_id))
#     if type == "checking":
#         select.select_by_visible_text("CHECKING")
#     elif type == "savings":
#         select.select_by_visible_text("SAVINGS")
#     rows =XlUtil.getrowcount(filename,"Sheet1")
#     columns = XlUtil.getcolumnount(filename,"Sheet1")
#     for row in range(2,rows):
#         Amount = XlUtil.readfromxl(filename,"Sheet1",row,2)
#         accountnumber = XlUtil.readfromxl(filename,"Sheet1",row,1)
#         amount = float(str.replace(Amount,'$',''))
#         if amount >= 200:
#             select = Select(self.browser.find_element_by_id(self.fromaccount_id))
#             select.select_by_visible_text(accountnumber)
#             self.browser.find_element_by_xpath(self.clickopenaccount_xpath).click()
#             time.sleep(3)
#             newaccountnumber = self.browser.find_element_by_xpath(self.newaccountid_xpath).text
#             break
#         else:
#             newaccountnumber = 00000
#             continue
#     return newaccountnumber