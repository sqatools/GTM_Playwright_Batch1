str1 = 'Hello'
str2 = "Python"
str3 = """We are Learning Python"""

print(str1, type(str1)) # Hello <class 'str'>
print("_"*50)
print(str2, type(str2)) # Python <class 'str'>
print("_"*50)
print(str3, type(str3)) # We are Learning Python <class 'str'>

print("_"*50)
############ String Methods  ###############
print(dir(str))
"""
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']
"""

str_a =  "Hello WE Are learNing pyThon"
print("upper() method :", str_a.upper())
# HELLO WE ARE LEARNING PYTHON

print("lower() method :", str_a.lower())
# lower() method : hello we are learning python

str_b = "HELLO"
print("isupper() method :", str_b.isupper())
# isupper() method : True

str_c = "python"
print("isupper() method :", str_c.islower())
# isupper() method : True

str_d = "good morNing"
print("title() method : ", str_d.title())
# Good Morning

str_e = "We are Learning Python Programming"
print("count method(), count of a:", str_e.count('a'))
# count method(), count of a: 3

print("index of any char/substring :", str_e.index("L"))
# index of any char/substring : 7

# split method():  this method split each word as list member.
str_f = "India is a Best Country"
output = str_f.split(" ")
print("output :", output) #  ['India', 'is', 'a', 'Best', 'Country']
print(output[3]) # Best

print("_"*50)
# replace method
str_g = "We Are Learning Python Programming Python"
output_g = str_g.replace("Python", "JAVA", 1)
print("output_g :", output_g)
# output_g :  We Are Learning JAVA Programming Python

print("_"*50)
# strip method :  This method remove, trailing spaces from any given string
str_h = "  Programming  "
print(str_h)
output_h = str_h.strip()
print(output_h)

print("_"*50)
# join method : any string or iterable datatype wants to join with any delimeter or string, then we can use join method
str_j = "Python"
lista = ["Hello", "Good", "Morning"]
tup_a = ("Python", "Is", "Easy", "to", "Learn")

output1 = "-".join(str_j)
print(output1) # P-y-t-h-o-n

output2 = " ".join(lista)
print(output2) # Hello Good Morning

output3 = " ".join(tup_a)
print(output3) # Python Is Easy to Learn

print("_"*50)
# find() method : This method return the index position of any char/substring from target string.
#               if target data is not available in the string, then it will return -1

str_l = "Hello Good Morning, Learning Python"
print("Index of Good :", str_l.find("Good"))
# Index of Good : 6

print("Index of non existing char , W:", str_l.find("W"))
# Index of non existing char , W: -1



