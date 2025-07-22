def addition(num1,num2):
    sumValue = num1+num2
    print("The additon values: ",sumValue)

#pass by value
print("Pass by values in args : ")
addition(10,10)

#pass by reference
x=10
y=10
print("pass by reference in args")
addition(x,y)

###############################################################
#we just list the values from the listValue1 and ListValue2
listValue1=[12,45,78,33,96]
listValue2=[1,2,3,4,5]
listValue3=[]

def addListValues(list1,list2):
    for i in range(len(list1)):
        print(i,list1[i],list2[i])

addListValues(listValue1,listValue2)

print('*'*75)
#################################################################
#We can use the addition method to add the values from listValue1 and listValue1


def addiing_two_listValues(list1,list2):
    for i in range(len(list1)):
        print(i,list1[i],list2[i])
        addition(list1[i],list2[i])
       #calling the method with args
addiing_two_listValues(listValue1,listValue2)

#########################################################
# we can put the values in separate list
print('*'*75)
def add_values(list1,list2):
    for i in range(len(list1)):
        print(i,list1[i],list2[i])
        addition(list1[i],list2[i])
        # append the added value into listValue3
        listValue3.append(list1[i] + list2[i])
        print("list of added values: ",listValue3)

add_values(listValue1,listValue2)

############################################################################33
print('*'*75)

str1 = "Hello we Are Learning Python"
def get_max_len_word(word):
    array_string=str1.split(" ")
    array_length=len(array_string)
    max_length=0
    array_max=""
    for eachword in array_string:
        print(eachword,len(eachword))
        if(len(eachword)>max_length):
            max_length=len(eachword)
            maxlengh_word=eachword
        else:
            continue
    return maxlengh_word

#print("_"*50)
output = get_max_len_word(str1)
print("output :", output)

################### function with default parameter value ###############
def multiplication(n1: int,n2:int=3, n3:int=3)-> int:
    """
    -> This is default parameter value funtion that return the multiplication of 2 numbers
    -> The sequence of default is like, first non-default and then default parameter we have to define
    -> If we dont provide value for default parameter while calling function then it will consider default value.
    -> If we provide value to default parameter while calling the function, it will overwrite default value.

    e.g. Example to call function
    Example 1: multiplication(10)
    Example 2: multiplication(10,20,30)
    Example 3: multiplication()
    # TypeError: multiplication() missing 1 required positional argument: 'n1'
    :param n1: first param to pass value
    :param n2: second param with default value
    :param n3: third param with default
    :return: expected return int value
    """
    multiply = n1*n2*n3
    return multiply
# here we are providing value for n1 and n2, n3 will take default value
result = multiplication(3)
print("multiplication result :", result)
#multiplication result : 27

# n1 = 4, n2=5  n3=8, default value will be overwrite by new value
result2 = multiplication(4, 5, 8)
print("result 2 :", result2)
#result 2 : 160

#result3= multiplication()
#print("result 3 :", result2)
#TypeError: multiplication() missing 1 required positional argument: 'n1'

#  Get documentation of the function
print(multiplication.__doc__)

print(len.__doc__)
#Return the number of items in a container.

result4 = multiplication('Hello', 2, 3)
print(result4)
#HelloHelloHelloHelloHelloHello

# get multiple return values from function and store in different variables
def math_operations(n1,n2):
    add=n1+n2
    multiply=n1*n2
    division=n1/n2
    return add,multiply,division

print('*'*75)
a,b,c=math_operations(20,10)
print('addition',a)
print('multiplication',b)
print('division',c)
'''
addition 30
multiplication 200
division 2.0
'''

#######################################################
# *args and **kwargs parameters
# args accept the values in tuple format
# kwargs accepts the values in dictionary
# args accepts the n number parameters
#kwargs accept the values as key value pair

def accept_different_values(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    for val in args:
        print(val)

    for k, v in kwargs.items():
        print(k, v)


accept_different_values(4, 5, 7, [4, 5, 6], (1, 3, 4), name='Rahul', email='rahul@gmail.com', phone=98789789)

"""
(4, 5, 7, [4, 5, 6], (1, 3, 4)) <class 'tuple'>
{'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 98789789} <class 'dict'>
4
5
7
[4, 5, 6]
(1, 3, 4)
name Rahul
email rahul@gmail.com
phone 98789789
"""

print("_"*50)
###################################################
# variables scope: global, local, non-local

var_p = 50 # global variable

def function1():
    var_q = 600 # local variable
    print("local variable :", var_q)

function1() # local variable : 600

def outer_function2():
    # var_r is local variable for outer function and non-local variable for inner function
    var_r = 500 # non loca variable

    def inner_fun1():
        var_s = 250 # local variable
        print("global var_p :", var_p)
        print("non local var_r:", var_r)
        print("local var_s:", var_s)

    inner_fun1()

outer_function2()


