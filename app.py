def addFunction(x, y):
    return x+y

def divFunction(x, y):
    return x/y

def subFunction(x, y):
    return x-y

def prodFunction(x, y):
    return x*y

def powFunction(x, y):
    return x**y

class Person:
    def __init__(self, name, address, telephone_number):
        self.name = name
        self.address = address
        self.telephone_number = telephone_number

class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        super().__init__(name, address, telephone_number)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

# person = Person('Nana Yaa', 'GE-669-88', '057-04-6841')
customer = Customer('Janet Aboi', 'GE-099-56', '057-456-8790', '020-5164-254', True)
