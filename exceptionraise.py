#catching specific exception
from tkinter import Y

try:
    a = int(input("Please enter the first number..."))
    b = int(input("The second number please"))
    if(a <0):
        raise TypeError
    c= x/y
    print("{} /{} = {}".format(a,b,c))
except ZeroDivisionError:
    print("Division by zero is impossible")
except ValueError:
    print("the data types are not proper")
except TypeError:
    print("Data types are not in range")
except NameError:
    print("Data items are not defined")
   
