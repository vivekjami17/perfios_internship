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

#In Python, a decorator is a function that modifies the behavior of another function without changing its code. Decorators are a powerful concept in Python and 
# allow developers to add functionality to existing functions or classes without modifying their source code[1][2][3].
#For example, consider the following code:

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

# In this example, we define a decorator my_decorator that adds some behavior before and after calling the decorated function. We then apply this decorator to the
# say_hello function using the @ syntax. When we call say_hello, it is actually calling the decorated version of the function that includes the additional behavior.
# Decorators can also take arguments and be used with classes as well as functions. For example:

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# In this example, we define a decorator repeat that takes an argument num_times. This decorator returns another decorator that wraps the original function and repeats it num_times. We then apply this decorator to the greet function using the @ syntax.
# In summary, decorators are a powerful feature in Python that allow developers to modify or enhance the behavior of functions or classes without changing their source code. They can be used to add functionality such as logging, caching, or authentication to existing code and make it more flexible and reusable.

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
# We can create modules and packages as per our own requirement

# Lamda Expression
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
#42
f(1)
# 43

# Venv 
# creating venv
python3 -m venv project_env
#pip list karke ek baar check karo
# activating venv
source project_env/bin/activate 
''' we ll be able to see environment name left of 
terminal 
once it is activated
'which python ' se kaunsa environment ka project chal rha he uska path dedega

version of python venv = version of python installed in system'''
# we can install specific packages that we can use for specific project
# 'pip freeze' gives the correct output so as to store them in 'requirements.txt' file
pip freeze > requirements.txt
# deactivating the environment
deactivate # It is the command for deactivation
# No longer , env in the prompt
rm -rf project_env # se pura virtual env directory ke sath delete ho jayega

# isiliye pehle ek directory banao, usme venv naam ka virtual environment banayenge
> mkdir my_project
> python3 -m venv my_project/venv
> source my_project/venv/binactivate # ( We activated the venv)
>  pip install -r requirements.txt # ( It will install all packages
# which are present in requirements.txt file)
> pip list #(ese ham compare kar sakte hein, pichle installed package set k sath)
> cd my_project
> ls #(bas venv hi he usme)
> touch script.py 
> ls #(script.py venv) he ab
# virtual environment should be in a way were it can be created and deleted 
# as no project files should be present in the venv folder as we will be deleting.
# we shouldn't commit our venv for source control
> deactive #(deactivated the virtual environment)
> rm -rf venv/ #(removing virtual env)
> python3 -m venv venv --system-site-packages#(jitne packages system (global) me he )
> 


#17th March

# Error Handling

#Error handling in Python is the process of detecting and responding to errors that occur during program execution. 
# Python provides a built-in mechanism for handling exceptions using the try-except statement
# [1]
# [2]
# [3]
#For example, consider the following code:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input")

#This code prompts the user to enter two integers and calculates their quotient. 
# If an exception occurs during this process, such as a division by zero or an invalid input, the corresponding except block is executed instead of 
# terminating the program. In this way, error handling allows programs to gracefully recover from errors and continue executing.
#Python also provides a finally clause that can be used to execute cleanup code regardless of whether an exception occurred or not[4][5]. For example:
try:
    # some code that may raise an exception
except SomeException:
    # handle the exception
finally:
    # cleanup code that always runs

#In summary, error handling is an important aspect of Python programming that allows programs to gracefully recover from errors and continue executing. 
# The try-except statement provides a built-in mechanism for handling exceptions, while the finally clause can be used to execute cleanup code regardless 
# of whether an exception occurred or not.

# Thread Pool and Process Pool

#In Python, thread pool and process pool can be created using the concurrent.futures module. 
#The ThreadPoolExecutor class can be used to create a thread pool, while the ProcessPoolExecutor class can be used to create a process pool
# [1]
# [2]
# [3]
#For example, to create a thread pool in Python, we can use the following code:
import concurrent.futures

def task(n):
    print(f"Task {n} is running")
    return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = [executor.submit(task, i) for i in range(5)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

#This code creates a thread pool with three worker threads and submits five tasks to the pool. 
#Each task simply prints a message and returns the square of its input. The as_completed function is used to wait for all tasks to complete and retrieve their results.
#Similarly, to create a process pool in Python, we can use the following code:
import concurrent.futures

def task(n):
    print(f"Task {n} is running")
    return n * n

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    results = [executor.submit(task, i) for i in range(5)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

#This code is similar to the previous example but uses a process pool instead of a thread pool. 
# Note that the task function is identical in both examples and can be run concurrently by multiple threads or processes.
#In summary, thread pools and process pools are useful tools for achieving parallelism in Python programs that have multiple independent tasks to perform. 
# They allow tasks to be executed concurrently by multiple threads or processes, which can improve performance by reducing overhead associated 
# with creating new threads or processes for each task.


# Common Libraries
# OS MODULE

#The os module in Python provides a portable way of using operating system-dependent functionality. 
# It offers a range of functions for working with files, directories, and other operating system tasks.
# [1]
# [2]
# [3]
# For example, consider the following code:
import os

# create a directory
os.mkdir("mydir")

# change the current working directory
os.chdir("mydir")

# create a file
with open("myfile.txt", "w") as f:
    f.write("Hello, world!")

# read the contents of the file
with open("myfile.txt", "r") as f:
    print(f.read())

# remove the file and directory
os.remove("myfile.txt")
os.chdir("..")
os.rmdir("mydir")

#In this example, we use various functions from the os module to create a directory, change the current working directory, create a file, read its contents, and 
# remove both the file and directory. The os module also provides functions for working with environment variables, running external commands, and more. For example:

import os

# get an environment variable
print(os.environ.get("PATH"))

# run an external command
result = os.system("ls -l")
print(result)

# In this example, we use the environ dictionary to get the value of an environment variable (PATH) and use the system function to run an external command (ls -l) and 
# print its result. In summary, the os module in Python provides a wide range of functions for working with files, directories, environment variables, and other 
# operating system tasks. These functions allow developers to write portable code that can work across different platforms and operating systems.

# SUBPROCESS

# In Python, the subprocess module is used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. The subprocess module 
# provides a way to execute shell commands or other programs from within a Python script.

# [1][2][3][4][5].

#The subprocess module provides several functions for executing external commands, including run, call, and Popen. These functions allow you to execute a command 
# and capture its output or error messages. For example:

import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True)
print(result.stdout.decode())

# In this example, we use the run function to execute the ls -l command and capture its output. The capture_output=True argument tells the function to capture both
#  stdout and stderr. We then print the output using the stdout.decode() method. The subprocess module also allows you to interact with running processes by 
# sending input or signals. For example:
import subprocess

p = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
p.communicate(input=b"Hello, world!\n")

# In this example, we use the Popen function to start a new process running the cat command. We then send input to the process using the communicate method.
# In summary, the subprocess module in Python provides a way to execute shell commands or other programs from within a Python script. It allows you to spawn new
#  processes, connect to their input/output/error pipes, and obtain their return codes. The module provides several functions for executing external commands 
# and interacting with running processes.

# DATETIME 

# In Python, the datetime module provides classes for working with dates and times. The module includes classes such as date, time, and datetime that allow developers to represent and manipulate dates and times in various formats[1][2][3][4][5].
# Here is an example of how to use the datetime module to work with dates:
     
import datetime

# create a date object
d = datetime.date(2023, 3, 20)

# print the date
print(d)

# get the current date
today = datetime.date.today()

# print today's date
print(today)

# calculate the difference between two dates
delta = today - d

# print the difference in days
print(delta.days)

# In this example, we create a date object representing March 20th, 2023. We then print this date using the print function. We also use the date.today() method to get today's date and calculate the difference between these two dates using subtraction.
# Here is an example of how to use the datetime module to work with times:

import datetime

# create a time object
t = datetime.time(15, 31, 0)

# print the time
print(t)

# get the current time
now = datetime.datetime.now().time()

# print the current time
print(now)

# In this example, we create a time object representing 3:31 PM. We then print this time using the print function. We also use the datetime.now() method to get the 
# current date and time and extract only its time component using .time() method.

# In summary, Python's datetime module provides classes for working with dates and times. These classes allow developers to represent and manipulate dates and times
# in various formats. The module includes methods for creating new objects representing specific dates or times as well as methods for performing arithmetic operations 
# on them.

# ARGPARSE

# In Python, argparse is a module that provides an easy way to parse command-line arguments and options. It allows developers to define the arguments that their 
# program expects and automatically generates help messages for users[1][2][3][4][5].

# Here is an example of how to use argparse to parse command-line arguments:

import argparse

# create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# add an argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# parse the arguments
args = parser.parse_args()

# print the sum of the integers
print(sum(args.integers))

# In this example, we create a new ArgumentParser object and add an argument called integers. This argument expects one or more integers as input. We then call the 
# parse_args() method to parse the command-line arguments and store them in a variable called args. Finally, we print the sum of the integers using the built-in sum() 
# function.
# To run this program from the command line, we would enter something like:

$ python myprogram.py 1 2 3 4 5

This would output:
15

# In summary, argparse is a module in Python that provides an easy way to parse command-line arguments and options. It allows developers to define expected arguments and 
# automatically generates help messages for users. By using argparse, developers can create user-friendly command-line interfaces for their programs.

# PANDAS


## Learn karne k liye kya kya chahiye
# Python ka
# data structures, functions, decorators, classes, modules, packeges, venv, error handling
# commonly used libraries :

# OS, subprocess
# datetime
# argparse
pandas
json
# threading
# pools(threadpool, processpool)