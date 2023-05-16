from customerTests import *
from customer0 import *

class Customer:
    """ This class represents a customer.  It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""

    def __init__(self, firstName, lastName, email):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def email(self):
        return self.__email

    @firstName.setter
    def firstName(self, firstName):
        if isinstance(firstName, str) and len(firstName.strip()) > 0:
            self.__firstName = firstName
        else:
            raise ValueError(
                f"First name cannot be blank. {type(firstName)} {firstName}")

    @lastName.setter
    def lastName(self, lastName):
        if isinstance(lastName, str) and len(lastName.strip()) > 0:
            self.__lastName = lastName
        else:
            raise ValueError(
                f"Last name cannot be blank. {type(lastName)} {lastName}")

    @email.setter
    def email(self, email):
        if isinstance(email, str) and "@" in email:
            self.__email = email
        else:
            raise ValueError(
                f"Email cannot be blank and must contain '@'. {type(email)} {email}")

    def __str__(self):
        return f'Customer(first Name: {self.firstName}, last Name: {self.lastName}, email: {self.email})'
