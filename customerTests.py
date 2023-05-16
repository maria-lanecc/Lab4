from customer import *

def testConstructor():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    print(f"Testing constructor with parameters. Expect customer Maria. {c}")

def testGetters():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    print(f"Testing getters. Expect individual attributes for customer Maria.")
    print(f"First Name: {c.firstName}, Last Name: {c.lastName}, Email: {c.email}")

def testPropertyGetters():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    print(f"Testing getters. Expect individual attributes for customer Maria.")
    print(f"First Name: {c.firstName}, Last Name: {c.lastName}, Email: {c.email}")

def testSetters():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    c.firstName = "Susan"
    c.lastName = "Evans"
    c.email = "evanss@lanecc.edu"
    print(f"Testing property setters. Expect individual attributes for customer Maria to change to Susan. {c}")

def testPropertySetters():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    c.firstName = "Susan"
    c.lastName = "Evans"
    c.email = "evanss@lanecc.edu"
    print(f"Testing property setters. Expect individual attributes for customer Maria to change to Susan. {c}")


def testPropertySettersWithValidation():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    try:
        c.firstName = int
    except ValueError as vErr:
        print("An exception was thrown setting First Name to an int")
        print(vErr)
    try:
        c.firstName = "    "
    except ValueError as vErr:
        print("An exception was thrown setting First Name to an empty string")
        print(vErr)
    try:
        c.lastName = int
    except ValueError as vErr:
        print("An exception was thrown setting Last Name to an int")
        print(vErr)
    try:
        c.lastName = "    "
    except ValueError as vErr:
        print("An exception was thrown setting Last Name to an empty string")
        print(vErr)
    try:
        c.email = int
    except ValueError as vErr:
        print("An exception was thrown setting Email to an int")
        print(vErr)
    try:
        c.email = "    "
    except ValueError as vErr:
        print("An exception was thrown setting Email to an empty string")
        print(vErr)


def testEncapsulation():
    c = Customer("Maria", "Carvalho", "monteirocarvalhom@my.lanecc.edu")
    try:
        c.__firstName = "Susan"
    except AttributeError as aErr:
        print("An exception was thrown setting private attribute")
        print(aErr)
    try:
        c.__lastName = "Evans"
    except AttributeError as aErr:
        print("An exception was thrown setting private attribute")
        print(aErr)
    try:
        c.__email = "evanss@lanecc.edu"
    except AttributeError as aErr:
        print("An exception was thrown setting private attribute")
        print(aErr)





