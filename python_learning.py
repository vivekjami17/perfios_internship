# lists in python
list = [1,2,3,"gfg",3.4]
print(list)

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List)

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List2)

# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])
# Getting the size of Python list
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

# Taking Input of a Python List
# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()
print('The list is:', lst)  # printing the list

# Adding Elements to a Python List
# append()
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# m2 insert (pos , val)
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)

# reversing
# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

# removing elements

# Dictionaries



# decorators
def div(a,b):
	return a/b

def smart_div(func):
	def inner(a,b):
		if a < b:
			a,b = b,a
		return func(a,b)

	return inner

div = smart_div(div)
div(2,4)

'''We are creating a mew function which takes function 
as a parameter and that's the beauty that this is not possible 
in all the languages so yes we can do that in Python because
 python is also a functional programming and then we can
define a function inside a function
which is actually replacing the code of
div behind the scene and then we before
calling div we are saying div is equal
to smart div and we are passing div so
basically we are changing the way they
works so that's how you can use
decorators in Python'''

# classes and objects in Python
class Person:
	name = "Harry"
	occupation = "SOftware Developer"
	networth = 10
	def info(self):
		print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()

b.name = "Nitika"
b.occupation = "HR"
# a.name = "Shubham"
# a.occupation = "Accountant"
# print(a.name, a.occupation)
a.info()

# Modules and Packages
# sudo pip3 install <package_name>
import math
# from math import factorial # math k andar se factorial ko import kiya
from math import log
# print(math.factorial(4))
from math import * # math lib me jitne bhi functions hein sabko uthalo
print(log(10000))
print(dir(math))
print(math.factorial(4))

# Lamda Expression
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
#42
f(1)
# 43
# We can create modules and packages as per our own requirement

## Learn karne k liye kya kya chahiye
# Python ka
data structures, functions, decorators, classes, modules, packeges, venv, error handling
commonly used libraries :

OS, subprocess
datetime
argparse
pandas
json
threading
pools(threadpool, processpool)