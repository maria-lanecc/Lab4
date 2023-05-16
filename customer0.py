from customerTests import *
from customer import *


class Customer:
    """ this class represents a product.  This version has public attributes and getters and setters. """

    # self refers to the calling object.  It is passed as the first parameter in each method definition
    def __init__(self, firstName, lastName, Email):
        """ init is a "magic method" that is used to construct or instantiate a product.
            p = Product() will create a product with default attribute values
            p = Product(1, "p001", "this is the description", 24.99, 10) will create a product for which each attribute has an explicit value"""
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = Email

    # getters or accessors provide access to each attribute
    def getfirstName(self):
        return self.firstName

    def getlastName(self):
        return self.lastName

    def getEmail(self):
        return self.Email

    # setters or mutators allow a programmer to change attribute value
    def setfirstName(self, firstName):
        self.firstName = firstName

    def setlastName(self, lastName):
        self.lastName = lastName

    def setEmail(self, Email):
        self.Email = Email

    def __str__(self):
        """ another "magic method" that converts a product object into a string.
            When you call print(p) or print(str(p)) this method is called "under the covers" on your behalf"""

        return f"Customer(First Name: {self.firstName}, Last Name: {self.lastName}, Email: {self.Email}, "
