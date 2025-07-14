a = 10
b = 20
print(a, b)

# assign one value to multiple variables
p = q = r = 100
print("p:", p)
print("q:", q)
print("r:", r)

# Assign different value to different variable at a time
x, y, z = 100, 200, 300
print("x :", x)
print("y :", y)
print("z :", z)


###### Rules to defined variable name ########
# 1. variable name can not contain space in the name
"""
var a = 500 # invalid variable
var_b = 600 # valid variable
"""

# 2. variable name can not start with numbers
# 123_var = 400 # invalid variable
# var_123 = 600 # valid

# 3. variable name can not special character except underscore
# var%abc = 400 # invalid
# var_xyz = 700 # valid

# 4. variable name can be any length
# abc_xyz_hello_python_programming = 400

n1 = 400
n2 = 500
print("addition :", n1+n2) # 900
print("multiplication :", n1*n2) # 200000
print("division :", n1//3) # output will be whole number # 133
print("division with single slace :", n2/6) # output will be a pointer value # 83.33333333333333
print("subtraction :", n1-n2) # -100
print("remainder operation :", 12%5) # 2
print("square of number :", 5**2) # 25
print("compare 2 values :", 50 == 40) # False


############################################################
# Python data types:
# 1. Numbers:
# i) Integer : when we defined any whole to variable then it is consider as integer data type

var1 = 50
print(var1, type(var1))
# 50 <class 'int'>

# ii) Float :  When we assign any pointer value to variable, then it is float data type.
var2 = 50.40
print(var2, type(var2))
# 50.4 <class 'float'>

print("_"*50)
# iii) Complex number : complex number is combination of real and imaginary number x+yj
# x = real
# y = imaginary

var3 = 40 + 50j
print(var3, type(var3))
print("real value :", var3.real)
# real value : 40.0

print("imaginary value :", var3.imag)
# imaginary value : 50.0


print("_"*50)
################### Sequential data type ############
# i). string :  When we define any value inside single/double/three quotes, then it is consider as string
str1 = 'Hello'
str2 = "Python"
str3 = """ We are learning Python 1234 """
print(str1, type(str1)) # Hello <class 'str'>
print(str2, type(str2)) # Python <class 'str'>
print(str3, type(str3)) # We are learning Python 1234  <class 'str'>


str4 = "Good"

"""
0  1    2   3   +ve indexing
g   o   o   d
-4 -3   -2 -1   -ve indexing
"""
# get first char with +ve indexing
print(str4[0]) # G

# get last char with -ve indexing
print(str4[-1]) # d



###############
# ii). list :  when we store multiple value in square bracket, then it is considered as list data type

list1 = [3, 4.5, 'Hello', [4, 5, 6], (2, 5), {'a': 234}, {5, 8, 9}, True]
print(list1, type(list1))
# [3, 4.5, 'Hello', [4, 5, 6], (2, 5), {'a': 234}, {8, 9, 5}, True] <class 'list'>


# get first value with +ve indexing
print(list1[0])  # 3
print(list1[-1]) # True



###############
# iii). tuple:   when we store multiple value in round bracket, then it is considered as tuple data type
tuple1 = (3, 4.5, 'Hello', [4, 5, 6], (2, 5), {'a': 234}, {5, 8, 9}, True)
print(tuple1, type(tuple1))
# (3, 4.5, 'Hello', [4, 5, 6], (2, 5), {'a': 234}, {8, 9, 5}, True) <class 'tuple'>

# get third value with +ve indexing
print(tuple1[2]) # Hello

# get reverse thord value with -ve indexing
print(tuple1[-3]) # {'a': 234}


print("_"*50)
######################## Dictionary #############
# dictionary : dictionary store data in key value format in curly braces {'a': 123}

dict1 = {'name': 'Rahul', 'age': 30, 'email': 'rahul@gamil.com', 'phone': 4567234123}
print(dict1, type(dict1))
# {'name': 'Rahul', 'age': 30, 'email': 'rahul@gamil.com', 'phone': 4567234123} <class 'dict'>

# get data with key
print(dict1['age']) # 30

# assign new key value pair to dict
dict1['Address'] = "Mumbai, Boriwali"
print("dict1 :", dict1)
# {'name': 'Rahul', 'age': 30, 'email': 'rahul@gamil.com', 'phone': 4567234123, 'Address': 'Mumbai, Boriwali'}

print("_"*50)
######################## set #############
# set = set data type store unique values in random order, duplicate data is not allowed

set1 = {3, 6, 7, 6, 'a', 'b', 3.5}
print(set1, type(set1))
# {'a', 3.5, 3, 'b', 6, 7} <class 'set'>



print("_"*50)
######################## Boolean #############
# Boolean : boolean data type has only 2 values True and False
var1 = True
var2 = False
print(var1, type(var1)) # True <class 'bool'>
print(var2, type(var2)) # False <class 'bool'>