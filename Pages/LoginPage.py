from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class LoginPage(BasePage):

    """By locators or Object Repositories"""
    EMAIL = (By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
    PASSWORD = (By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')
    SIGNUP_LINK = (By.LINK_TEXT, "Register")
    XPATH_WELCOME_MSG = (By.XPATH, '//*[@id="leftPanel"]/p/b')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    """Page Actions"""

    """Used to get login page title"""
    def get_login_page_title(self, title):
        self.get_title(title)

    """Used to validate if sign_up link exits"""
    def is_sign_up_link_exits(self):
        return self.is_visible(self.SIGNUP_LINK)

    """Used to login to App and Assert Welcome Message after login is successful"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        self.driver.implicitly_wait(10)
        WELCOME_MSG = self.get_element_text(self.XPATH_WELCOME_MSG)
        assert WELCOME_MSG