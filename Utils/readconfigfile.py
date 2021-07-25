import configparser

config=configparser.RawConfigParser()
config.read("C:\\Commit Projects\\Automate-Parabank-Parasoft\\Config\\config.ini")
class Getinfoconfig:
    @staticmethod
    def get_weburl():
        Weburl=config.get("inputs","weburl")
        return  Weburl

    @staticmethod
    def get_username():
        username = config.get("inputs", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("inputs", "password")
        return password

    @staticmethod
    def get_firstname():
        firstname = config.get("inputs", "firstname")
        return firstname

    @staticmethod
    def get_lastname():
        lastname = config.get("inputs", "lastname")
        return lastname

    @staticmethod
    def get_address():
        address = config.get("inputs", "address")
        return address

    @staticmethod
    def get_city():
        city = config.get("inputs", "city")
        return city

    @staticmethod
    def get_zipcode():
        zipcode = config.get("inputs", "zipcode")
        return zipcode

    @staticmethod
    def get_state():
        state = config.get("inputs", "state")
        return state

    @staticmethod
    def get_phone():
        phonenumber = config.get("inputs", "phone")
        return phonenumber

    @staticmethod
    def get_ssn():
        ssn = config.get("inputs", "ssn")
        return ssn

    @staticmethod
    def get_payeename():
        payeename = config.get("inputs", "payeename")
        return payeename

    @staticmethod
    def get_payeeaddress():
        payeeaddress = config.get("inputs", "payeeaddress")
        return payeeaddress

    @staticmethod
    def get_payeecity():
        payeecity = config.get("inputs", "payeecity")
        return payeecity

    @staticmethod
    def get_payeestate():
        payeestate = config.get("inputs", "payeestate")
        return payeestate

    @staticmethod
    def get_payeezip():
        payeezip = config.get("inputs", "payeezip")
        return payeezip

    @staticmethod
    def get_payeeph():
        payeeph = config.get("inputs", "payeeph")
        return payeeph

    @staticmethod
    def get_payeeaccount():
        payeeaccount = config.get("inputs", "payeeaccount")
        return payeeaccount

    @staticmethod
    def get_payeeamount():
        amount = config.get("inputs", "amount")
        return amount