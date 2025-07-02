# Class and Object - Task 4
class Customer:
    def __init__(self, customer_name="", email="", phone_number=""):
        self.__customer_name = customer_name
        self.__email = email
        self.__phone_number = phone_number

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, value):
        self.__customer_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    def display_customer_details(self):
        print(f"Customer Name: {self.__customer_name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phone_number}")

    def __str__(self):
        return f"Customer: {self.__customer_name}, {self.__email}"