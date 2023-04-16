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

# =================================================================
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
print(customer.telephone_number)
print(customer.name)
print(customer.customer_number)
print(customer.mailing_list)


# ------------------------------------------------------------------------------
from datetime import date
print(date.today())

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + 'parsecs is '+ str(lightyears)+ 'lightyears')

print('Calculator program')
first_num = input('first_num: ')
second_num = input('second_num: ')
print(int(first_num) + int(second_num))

parsecs_input = input('Input number of parsecs: ')
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + 'parsecs is ' + str(lightyears) + ' lightyears')

# from datetime import *
# from dateutil.relativedelta import *
# now = datetime.now()
# print(now)

# now = now + relativedelta(months=1, weeks=1, hour=10)

# print(now)

# -------------------------------------------------------------------
age = 8
try:
    print(age) 
except:
    print('Error: Variable not defined')


import sys
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
try:
    result = number1/number2 #not a global variable 
except ZeroDivisionError:
    print('Error: Cannot divide by zero')
    sys.exit(1)
finally: #executes whether there was an error or not 
    print('Code executed successfully')
print(f'Division: {result}')
