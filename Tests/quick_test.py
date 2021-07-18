from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time
import requests

"""
 Enter username and password in the popup-window in selenium Python 
"""

URL = "https://parabank.parasoft.com/parabank/index.htm"
logger = logging.getLogger(__name__)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.implicitly_wait(5)
username = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input').send_keys('john')
password = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input').send_keys('dong')
login = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')
login.send_keys(Keys.ENTER)
success = driver.find_element(By.XPATH, '//*[@id="leftPanel"]/p/b')
print(success.text)
logger.info(success.text)
# driver.implicitly_wait(3)

# assert login_successful_div.text, "Please check your credentials and try again"
# Added Static wait just to slow down the process and validate in UI
time.sleep(5)
driver.quit()
