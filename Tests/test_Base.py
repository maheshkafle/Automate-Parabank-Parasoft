import pytest
from Utils.readconfigfile import Getinfoconfig
from Utils.CustomLogger import Logsetup

# @pytest.mark.fixtures()
class BaseTest:
    pass

    weburl = Getinfoconfig.get_weburl()
    firstname = Getinfoconfig.get_firstname()
    lastname = Getinfoconfig.get_lastname()
    username = Getinfoconfig.get_username()
    password = Getinfoconfig.get_password()
    logger = Logsetup.getlogparabank()