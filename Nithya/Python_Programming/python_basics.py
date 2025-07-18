a=10
b=20
print(a,b)

#assign one value to multiple variables

p=q=r=100
print("p: ",p)
print("q: ",q)
print("r: ",r)

#Assign different values to different variables at a time
x,y,z=100,200,300
print("x: ",x)
print("y: ",y)
print("z: ", z)

"""
## Rules to defined a variable name ##
# 1. Varaible name cannot contain space in the name

var a = 500  # Invalid Variable
var_a =600 # Valid Variable

#2. Variable name cannot start with numbers
123_var  #Invalid
var_123 =100 Valid

#3. Variable name cannot contain special character except underscore
var@123 =100 invalid
var_123=100 valid

#4. Variable name can be any length
abc_xyz_hello_python_programming=400

"""

n1=100
n2=100
print("addition : " ,n1+n2)
print("subtraction : ", n1-n2)
print("Multiplication : ", n1*n2)
print("division : ", n1//n2) # Output will be whole number
print("division with single slash : ", n1/n2) #output will be a pointer value 1.0
print("Modulus operation : ", n1%10) #0
print("square of numebr : ", 5**2) #25
print("compare 2 values : ", 50==40) #false


########################################################################3333
# Different type of data types
# 1. Number
    # i).Integer : When we define any whole number to a variable then it is consider as integer data type.
var1=50
print(var1, type(var1)) #50 <class 'int'>

    #ii) Float: When we assign any pointer value to variable, then it is float data type.
var2=50.4
print(var2,type(var2)) # 50.4 <class 'float'>

print("-"*50)
    #iii)Complex Number: Complex number is combination of real and imaginary number x+yj
            # x - real number
            # yj - imaginary number
var3=40+50j
print(var3,type(var3))
print("real values : ",var3.real)
print("imaginary values : ",var3.imag)

"""

(40+50j) <class 'complex'>
real values :  40.0
imaginary values :  50.0
"""

########################### Sequential data type ##################################################
#It has three data type
#i). String: When we define any value inside single, double, triple quote then it is consider as string
str1='Hello'
str2="Python"
str3=""" we are learning python. """
print(str1,type(str1)) # Hello <class 'str'>
print(str2,type(str2)) # Python <class 'str'>
print(str3,type(str3)) # we are learning python.  <class 'str'>

#Why it is called as sequential data type there is postive and negative indexing
str4="good"

"""
0   1  2  3
g   o  o  d
-4 -3 -2 -1
"""
# get first character with positive indexing
print(str4[0])  # g

# get last character with negative indexing
print(str4[-1]) # d

############################################################33
# iii). List : When we store multiple values in square bracket, then is considered as list data type.

list1 = [3,4,5,'Hello', [1,2,3], (2,3),{'a': 234}, {4,5,6},True]
print(list1,type(list1)) #<class 'list'> <class 'list'>

# get first value with -ve index
print(list1[0]) #3
print(list1[-1]) #True

############################################################33
# iiii). tuple : When we store multiple values in round bracket, then is considered as tuple data type.
# list and tuple will work in similar way only difference is list can be modifiable but tuple cannot

tuple1 = (3,4,5,'Hello', [1,2,3], (2,3),{'a': 234}, {4,5,6},True)
print(tuple1,type(tuple1)) #<class 'list'> <class 'list'>
# (3, 4, 5, 'Hello', [1, 2, 3], (2, 3), {'a': 234}, {4, 5, 6}, True) <class 'tuple'>

# get third value with +ve indexing
print(tuple1[3]) #Hello

# get reverse third value
print(tuple1[-3]) #{'a': 234}

######################## dictionary data type ##########################
# as list and tuple have a sequence to store the data but
# dictionary is going to store the data in key value pair in curly braces {'a':123}

dict1 = { 'name': 'Rahul', 'age': ' 33', 'email': 'rahul@gmail.com', 'phone': '123456788'}
print(dict1,type(dict1))
#{'name': 'Rahul', 'age': ' 33', 'email': 'rahul@gmail.com', 'phone': '123456788'} <class 'dict'>


print(dict1['age']) # 33

#assign new key value pair
dict1['Address'] = '8 th street, Mumbai'
print('dict1:', dict1)
#dict1: {'name': 'Rahul', 'age': ' 33', 'email': 'rahul@gmail.com', 'phone': '123456788', 'Address': '8 th street, Mumbai'}

print('_'*50)

######################## set data type ##########################
# It store the data. It does not follow the indexing.
#It does not show the sequential order the purpose of the set is store to unique value
#It can store unique values in random order and duplicate data is not allowed

set1={3,5,7,23,45,5,'a','Raja',3.5}
print(set1,type(set1))
#{3.5, 3, 5, 7, 'Raja', 45, 23, 'a'} <class 'set'>
#5 is duplicate but store one time

################### boolean data type ###############################

var1= True
var2 = False
print(var1),type(var1) #True
print(var2),type(var2) #False