import threading
import re

class Customer:
    def __init__(self,c_id,name="None",age="None",phone="None",email="None"):
        self.c_id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_id(c_id):
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        return name.isalpha()

    @staticmethod
    def check_age(age):
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        return  bool(re.match(r"^1[3-9]\d{9}$",phone))

    @staticmethod
    def check_email(email):
        return bool(re.match(r"^[a-zA-Z0-9_.+-]+$",email))

    def __str__(self):
        return f"cid:{self.c_id:<20},name:{self.name:<20},age:{self.age:<20},phone:{self.phone:<20},email:{self.email:<20}"


if __name__ == '__main__':
    c1 = Customer("001")
    print(c1)