"""

a=10
b=20
print(a,b)

#Assign one value to multiple variables

p = q = r = 84

print("p:", p)
print("q", q)
print("r",r)

#Assign different value to different variables

x,y,z = 100, 200, 300

print("x :",x)
print("y :",y)
print("z",z)


n1 = 400
n2 = 500
print("addition:", n1+n2)

print("multiplication:", n1*n2)

print("division:", n1//n2)

print("division with single space:", n2/6)

print("substraction:", n1-n2)

print("remainder:", 12%5)

print("square:", 5**2)

print("compare two values:", 50 == 50)


from typing import Tuple

#Python data types
#1. Numbers - Any whole number

var1 = 84
print(var1, type(var1))

# Float - when we add decimal/ pointer to the number

var2 = 84.84
print(var2, type(var2))

# complex number

var3 = 40 + 50j
print(var3, type(var3))

print("real value: ", var3.real)

print("imaginary value:", var3.imag)

#String
str1 = 'hello'
str2 = "Python"
str3 = 'We are learning Python'
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))

str4 = "Good"

0  1  2  3
G  o  o  d
-4 -3 -2 -1

print(str4[0])
print(str4[3])
print(str4[-4])

# When we store multiple value in square bracket, then it is considered as list data type

list1 = [3, 4.5, 'Hello', [4,5,6], (2,5), {'a':234}, {5,8,9}, True]
print(list1, type(list1))
print(list1[1])
print(list1[-1])
"""
from operator import truediv

#Tuple. When we store multiple value in round bracket, then it is considered as Tuple data type
tuple1 = (3, 4.5, [84,85], {'a':234}, True)
print(tuple1)
#Get 3rd value of +ve indexing
print(tuple1[2])
#Get reversed 1st value with -ve indexing

print(tuple1[-1])
print(tuple1[-2])

print("_"*50)
#Dictionary store data in key value format in curly braces {'a', 123}
dict1 = {'Name' : 'Abhi', 'Age' : 44, 'email' : 'test@test.com', 'phone' : 8477777777}

print(dict1['Name'])
#Assign new key value pair to dict
dict1['Address'] = "Bavdhan, Katraj"
print("dict1", dict1)

print('_'*50)

#Set is data type that store unique values in random order, duplicate data is not allowed

set1 = {3, 6 , 9 , 'a', 'A'}
print(set1, type(set1))

#Boolean data types

var1 = True
var2 = False

print(var1, type(var1))
print(var2, type(var2))