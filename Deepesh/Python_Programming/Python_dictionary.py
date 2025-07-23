dict1 = {'key': 'value'}
"""
->  dict is mutable data type
->  dict only contains unique keys, duplicate keys are not allowed.
->  only immutable data type can be key in the dict. e.g int, float, string, tuple, boolean.
->  All the data type can be value in the dictionary.
->  Dict store values in LIFO( LAST IN FIRST OUT ) concept.
"""

dict2 = {'a': 234, 'b': 567, 'c': 789, 'a': 333}
print(dict2, type(dict2))
# {'a': 333, 'b': 567, 'c': 789} <class 'dict'>

# get value of the dictionary
print(dict2['b'])  # 567

# assign new key value pait to the dictionary
dict2['d'] = 700
print("dict2 :", dict2)
# dict2 : {'a': 333, 'b': 567, 'c': 789, 'd': 700}

# delete key value pair from dictionary
del dict2['b']
print("dict2 :", dict2)
# {'a': 333, 'c': 789, 'd': 700}

print("_" * 50)
###############################################
dict3 = {'p': 3, 'q': 4, 'r': 5, 's': 6}

print(dict3.items())

for k, v in dict3.items():
    print(k, ":", v, ":", v ** 2)

"""
p : 3 : 9
q : 4 : 16
r : 5 : 25
s : 6 : 36
"""

M, N = (40, 50)
print("M:", M)  # 40
print("N :", N)  # 50

print("_" * 50)
################## Methods in dictionary ###############
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# update method:  this method combine one dict data to another dict.
d1 = {'A': 234, 'B': 567}
d2 = {'C': 253, 'D': 890}
d2.update(d1)
print("d2 :", d2)  # {'C': 253, 'D': 890, 'A': 234, 'B': 567}
print("d1 :", d1)  # {'A': 234, 'B': 567}

#################
# keys() and values() method:
d3 = {'C': 253, 'D': 890, 'A': 234, 'B': 567}
print("list of keys :", d3.keys()) # dict_keys(['C', 'D', 'A', 'B'])
print("list of values :", d3.values()) # dict_values([253, 890, 234, 567])

####################
# GET DATA WITH THE HELP OIF VALUE
# Get Method
print("get value of A :", d3.get("A"))
# get value of A : 234


print("_"*50)
####################
# pop method :  This method remove the data from dictionary with the help of values and return it.
d4 = {'C': 253, 'D': 890, 'A': 234, 'B': 567}
result =  d4.pop('B')
print("removed value :", result) # 567
print("d4 :", d4) #  {'C': 253, 'D': 890, 'A': 234}

print("_"*50)
####################
# popitem method :  This method remove the key value which one is updated at end of dict.
d4 = {'C': 253, 'D': 890, 'A': 234, 'B': 567, 'E': 700}
val = d4.popitem()
print("removed data:", val)  # ('E', 700)
print(d4) # {'C': 253, 'D': 890, 'A': 234, 'B': 567}


print("_"*50)
################## Programs ######################
# write a python program to calculate the bill amount on the basis items purchased.

fruit_price = {'Apple': 10, 'Banana': 20, 'Mango': 30, 'watermelon': 35}
fruit_inventory = {'Apple': 100, 'Banana': 200, 'Mango': 250, 'watermelon': 50}
purchase_items = {'Apple': 5, 'Banana': 10, 'Mango': 15, 'watermelon': 5}

total_bill = 0
for f_name, f_price in fruit_price.items():
    # Get number of items purchased
    pur_item = purchase_items[f_name]
    # Update inventory with number of items purchased
    fruit_inventory[f_name] = fruit_inventory[f_name] - purchase_items[f_name]
    # calculate each fruit bill
    fruit_bill = f_price*pur_item
    # show all required values in print
    print(f_name, f_price, pur_item, fruit_bill)
    # store fruit bill amount in total bill
    total_bill = total_bill + fruit_bill

print("_"*50)
print("Total bill amount :", total_bill)
print("Updated inventory :", fruit_inventory)

