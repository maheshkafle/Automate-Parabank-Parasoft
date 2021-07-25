import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def init_driver(request):
     browser = webdriver.Chrome(ChromeDriverManager().install())
     return browser