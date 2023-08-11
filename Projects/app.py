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

# -----------------------------------------------------------------------------------------------------------------
#%%
import numpy as np

def find_max(x):
    """A simple function to find the largest value in a numpy array.

    Args:
        x (array[float]): an array of numbers of size n

    Returns:
        float: The maximum value in x.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    max_value = np.max(x)
    return max_value
    

my_array = np.array([3, 7, 1, 9, 4, 5])
max_value = find_max(my_array)
print(max_value)

#%%
import pennylane as qml
import numpy as np

dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def circuit(x):
    qml.RZ(x, wires=0)
    qml.CNOT(wires=[0,1])
    qml.RY(x, wires=1)
    return qml.expval(qml.PauliZ(1))

result = circuit(0.543)

import matplotlib.pyplot as plt
qml.drawer.use_style("black_white")
fig, ax = qml.draw_mpl(circuit)(np.pi/4, 0.7)
plt.show()

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
import numpy as np

dev = qml.device('default.qubit', wires=2)

theta = Parameter('θ')

qc = QuantumCircuit(2)
qc.rz(theta, [0])
qc.rx(theta, [0])
qc.cx(0, 1)

@qml.qnode(dev)
def quantum_circuit_with_loaded_subcircuit(x):
    qml.from_qiskit(qc)({theta: x})
    return qml.expval(qml.PauliZ(0))

angle = np.pi/2
result = quantum_circuit_with_loaded_subcircuit(angle)
# %%
