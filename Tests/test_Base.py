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
    address = Getinfoconfig.get_address()
    logger = Logsetup.getlogparabank()
    city = Getinfoconfig.get_city()
    state = Getinfoconfig.get_state()
    zipcode = Getinfoconfig.get_zipcode()
    phonenumber = Getinfoconfig.get_phone()
    ssn = Getinfoconfig.get_phone()
    username = Getinfoconfig.get_username()
    password = Getinfoconfig.get_password()
    payeename = Getinfoconfig.get_payeename()
    payeeaddress = Getinfoconfig.get_payeeaddress()
    payeecity = Getinfoconfig.get_payeecity()
    payeestate = Getinfoconfig.get_payeestate()
    payeezip = Getinfoconfig.get_payeezip()
    payeeph = Getinfoconfig.get_payeeph()
    payeeaccount = Getinfoconfig.get_payeeaccount()
    amount = Getinfoconfig.get_payeeamount()