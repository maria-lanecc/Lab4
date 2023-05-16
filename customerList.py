from customer import *


class CustomerList:
    """This class represents a list of customer objects """

    def __init__(self):
        self.customers = []

    def __len__(self):
        return len(self.customers)

    def __getitem__(self, i):
        return self.customers[i]

    def __setitem__(self, i, customer):
        if isinstance(customer, Customer):
            self.customers[i] = customer
        else:
            raise ValueError("Can only set a Customer object in a CustomerList")

    def __delitem__(self, i):
        del self.customers[i]

    def __str__(self):
        return "\n".join(str(c) for c in self.customers)

    def append(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
        else:
            raise ValueError("Can only append a Customer object to a CustomerList")

    def pop(self, i=-1):
        return self.customers.pop(i)

    def remove(self, customer):
        if isinstance(customer, Customer):
            self.customers.remove(customer)
        else:
            raise ValueError("Can only remove a Customer object from a CustomerList")

    def index(self, customer):
        return self.customers.index(customer)

    def __contains__(self, customer):
        return customer in self.customers

    def __iter__(self):
        return iter(self.customers)

    def get_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        raise ValueError(f"No customer with email {email} found in the list")

