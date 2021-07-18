import time

import pytest
from selenium import  webdriver
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    time.sleep(3)
    # web_driver.close()