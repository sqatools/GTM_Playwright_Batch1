def addition(num1, num2):
    sum_value = num1+num2
    print("Addition :", sum_value)

# pass by value
#addition(30, 50)

# pass by reference
x = 100
y = 300
#addition(x, y)


list1 = [3, 5, 7, 8, 12]
list2 = [7, 8, 23, 56, 78]
list3 = []

def add_list_values(l1, l2):
    l3 = []
    for i in range(len(l1)):
        print(i, l1[i], l2[i])
        addition(l1[i], l2[i])
        # append method add value to the list at end of list
        l3.append(l1[i]+l2[i])
    print("list3 :", l3)

#print("_"*50)
#add_list_values(list1, list2)

str1 = "Hello we Are Learning Python"
def get_max_len_word(s1):
    word_list = s1.split(" ")
    print(word_list)
    max_len = 0
    max_len_word = ''
    for word in word_list:
        word_len = len(word)
        print(word, word_len)
        if word_len > max_len: # 5 > 0 | 2 > 5 | 3 > 5 | 8 > 5 | 6 > 8
            max_len = word_len # 5, 8
            max_len_word = word # Hello, Learning
        else:
            continue

    return max_len_word

#print("_"*50)
# output = get_max_len_word(str1)
# print("output :", output)


################### function with default parameter value ###############

def multiplication(n1: int, n2:int=6, n3:int=7) -> int:
    """
    -> This is default parameter value function that return the multiplication of 2 numbers
    -> The sequence of default is like, first non-default and then default parameter we have to define.
    -> If we don't provide value for default parameter while calling function then it will consider default value
    -> If we provide value to default parameter while calling the function, it will overwrite default value.

    e.g. Example to call function
    Example1 :  multiplication(10)
    Example2 :  multiplication(10, 20, 30)
    Example3 :  multiplication()
    # TypeError: multiplication() missing 1 required positional argument: 'n1'

    :param n1: first param to pass value
    :param n2: second param with default value
    :param n3: thord param with default
    :return int: expected return int value
    """
    multiply = n1*n2*n3
    return multiply

# here we are providing value for n1 and n2, n3 will take default value
result = multiplication(3)
print("multiplication result :", result)
# multiplication result : 126

# n1 = 4, n2=5  n3=8, default value will be overwrite by new value
result2 = multiplication(4, 5, 8)
print("result 2 :", result2)


#  Get documentation of the function
print(multiplication.__doc__)

print(len.__doc__)

# multiplication()
# TypeError: multiplication() missing 1 required positional argument: 'n1'

# result3 = multiplication('Hello', 2, 3)
# print(result3)



# get multiple return values from function and store in different variables
def math_operations(n1, n2):
    add =n1+n2
    multiply = n1*n2
    division = n1//n2
    return add, multiply, division

print("_"*50)
a, b, c = math_operations(20, 10)
print("addition :", a)
print("multiplication :", b)
print("division :", c)


#######################################################
# *args and **kwargs parameters
# args accept the values in tuple format
# kwargs accepts the values in dictionary
def accept_different_values(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    for val in args:
        print(val)

    for k, v in kwargs.items():
        print(k, v)


accept_different_values(4, 5, 7, [4, 5, 6], (1, 3, 4), name='Rahul', email='rahul@gmail.com', phone=98789789)

print("_"*50)
###################################################
# variables scope: global, local, non-local

var_p = 50 # global variable

def function1():
    var_q = 600 # local variable
    print("local variable :", var_q)

function1()


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
