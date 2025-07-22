list1 = [3, 5.6, 'Hello', [4, 5, 6], (4, 6, 7), {'a': 123, 'b': 567}, {4, 7, 2, 5, 7}, True]
print(list1, type(list1))
# [3, 5.6, 'Hello', [4, 5, 6], (4, 6, 7), {'a': 123, 'b': 567}, {2, 4, 5, 7}, True] <class 'list'>

# get value using indexing
print(list1[2]) # Hello
print(list1[3]) # [4, 5, 6]
print(list1[3][1]) # 5
print(list1[-3]) # {'a': 123, 'b': 567}
print(list1[-3]['a']) # 123

# slicing in list :  list1[start: end value:  step value]
print(list1[0:5:1])  # [3, 5.6, 'Hello', [4, 5, 6], (4, 6, 7)]
print(list1[4:0:-1]) # [(4, 6, 7), [4, 5, 6], 'Hello', 5.6]
print(list1[4::-1])  # [(4, 6, 7), [4, 5, 6], 'Hello', 5.6, 3]
print(list1[1:-1:1]) # [5.6, 'Hello', [4, 5, 6], (4, 6, 7), {'a': 123, 'b': 567}, {2, 4, 5, 7}]

url = "https://www.facebook.com"
print(url[12::1]) # facebook.com

print("_"*50)
################# List Methods ##################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

list2 = [4, 6, 8, 2]

# Append method :  Add value at end of the list
list2.append(100)
print("list2 :", list2) # list2 : [4, 6, 8, 2, 100]

# insert method:  insert value at specific index
list2.insert(1, 200)
print("list2 :", list2) # [4, 200, 6, 8, 2, 100]


# extend method: add one list data to another list
l1 = [5, 7, 8, 2]
l2 = [11, 44, 66]
# l1.extend(l2)
# print("l1 list :", l1) # [5, 7, 8, 2, 11, 44, 66]

# list concatenation: we can combine 2 list2 data with the help of list concatenation.
l3 = l1 + l2
print("list3 :", l3)  # [5, 7, 8, 2, 11, 44, 66]

# list value multiplication
l4 = [7, 8, 9]
print(l4*5) # [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]

print("_"*50)
####### remove data from list ##########
# remove method :  remove any specific value from list
l5 = [5, 7, 9, 23, 45]
l5.remove(23)
print("l5 :", l5) # [5, 7, 9, 45]


##############################
# pop method: This method remove value with help of index position and return.
l6 = [5, 7, 9, 23, 45, 77, 23, 9]
# default index is -1
v1 = l6.pop()
print("removed value :", v1) # 23
print("l6 :", l6) # [5, 7, 9, 23, 45, 77]

v2 = l6.pop(2)
print("removed value :", v2) # 9
print("l6 :", l6) # [5, 7, 23, 45, 77]

######### sort method ###########
# sort method :  sort list value
# sort in ascending order
l7 = [6, 8, 9, 23, 56, 1, 2]
l7.sort()
print("l7 :", l7) # [1, 2, 6, 8, 9, 23, 56]

# sort in descending order
l8 = [6, 8, 9, 23, 56, 1, 2]
l8.sort(reverse=True)
print("l8 :", l8) # [56, 23, 9, 8, 6, 2, 1]

print("_"*50)
######### reverse method ###########
# reverse method :
l9 = [6, 8, 9, 23, 56, 1, 2, 100]
l9.reverse()
print("l9 :", l9) # [100, 2, 1, 56, 23, 9, 8, 6]


l10 = [6, 8, 9, 23, 56, 1, 2, 100]
# reverse list values with slicing
print(l10[::-1]) # [100, 2, 1, 56, 23, 9, 8, 6]
# l10[-1:-len(list)-1: -1]
print(l10[-1:-9:-1]) # [100, 2, 1, 56, 23, 9, 8, 6]

print("_"*50)
######### count method ###########
l11 = [23, 6, 8, 9, 23, 56, 1, 2, 100, 23]
print("count of 23 :", l11.count(23))
# count of 23 : 3

print("_"*50)
######### copy method ###########
# shallow copy: in shallow we create a reference of list and if we do changes in any of the list
# then changes will reflect in both the lists.

l1_a = [4, 6, 8, 23, 1]
l2_b = l1_a

l1_a.append(300)
l2_b.append(200)
print("l1_a:", l1_a) # [4, 6, 8, 23, 1, 300, 200]
print("l2_b :", l2_b) # [4, 6, 8, 23, 1, 300, 200]

# Deep copy :  In deep copy we have to use copy method and create new copy list data.
#              if we do changes in any of the list, then respective list will be modified.

list_p = [6, 7, 2, 5, 16]
list_q = list_p.copy()
list_q.append(100)
list_p.append(400)

print("list_p :", list_p) # [6, 7, 2, 5, 16, 400]
print("list_q :", list_q) # [6, 7, 2, 5, 16, 100]

print("_"*50)
############################## list comprehension ############################

list1 = [5, 7, 8, 12, 9, 13, 15, 2, 6]
# output = [8, 12, 2, 6]
output = []
for val in list1:
    if val%2 == 0:
        print(val)
        output.append(val)

print("output :", output) # [8, 12, 2, 6]

result = [x for x in list1 if x%2 ==0]
print(result)
# [8, 12, 2, 6]


##################################
result1 = []
for val in list1:
    if val%2 == 0:
        result1.append((val, 'even'))
    else:
        result1.append((val, 'odd'))

print("result1 :", result1)
# list comprehension with if else condition
result = [(val, 'even') if val%2 == 0 else (val, 'odd') for val in list1]
print(result)
# [(5, 'odd'), (7, 'odd'), (8, 'even'), (12, 'even'), (9, 'odd'), (13, 'odd'), (15, 'odd'), (2, 'even'), (6, 'even')]

