"""
range(start value, end value, step value)
-> output will include the start value and exclude end value e.g range(2, 5, 1) :  2, 3, 4
  range(1, 10, 2) : 1, 3, 5, 7, 9
-> default start value is zero and step value is 1. e.g range(5) : 0, 1, 2, 3, 4
"""

# range(2, 5, 1) :  2, 3, 4
for i in range(2, 5, 1):
    print(i)

print("_"*50)

# range(1, 10, 2) : 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)


print("_"*50)
# range(5) : 0, 1, 2, 3, 4
for i in range(5):
    print(i)


# print("_"*50)
# for i in range():
#     print(i)

# TypeError: range expected at least 1 argument, got 0

print("_"*50)
###############################
# write a program to print table of any number
for i in range(1, 11):
    print(i, "*", 5, "=", i*5)

"""
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50

Process finished with exit code 0


"""

print("_"*50)
################## program to get even number from 1 to 50 ##############

for i in range(1, 50):
    if i%2 == 0:
        print(i)
    else:
        continue


print("_"*50)
############## Apply loop on string #############
str1 = "Good Morning"
for char in str1:
    print(char)


print("_"*50)
# get vowels from string
str2 = "Good Morning"
vowels = "aeiou"
for char in str1:
    if char in vowels:
        print(char)
    else:
        continue

print("_"*50)
############## Apply loop on list #############
list1 = [30, 23, 45, 67, 12]
for val in list1:
    print(val)

print("_"*50)
###### get square of even value from list ###
list2 = [3, 5, 7, 2, 8, 4, 12]
for val in list2:
    if val%2 == 0:
        print(val, ":", val**2)
    else:
        continue

print("_"*50)
############## Apply loop on dictionary #############
dict1 ={'a': 12, 'b': 20, 'c': 25}
for key, val in dict1.items():
    print("key :", key, "value:", val, val**2)


print("_"*50)
############## Apply loop on set #############
set1 = {3, 5, 7, 3, 7, 8, 9}
for val in set1:
    print(val)

"""
3
5
7
8
9
"""
print("_"*50)
#####################continue and break #################
# continue keyword :  when the continue condition met, loop will move ahead to next interation value.
for i in range(1, 11):
    if i in [3, 5, 7]:
        continue
    print(i, end=" ")

# 1 2 4 6 8 9 10
print()

# break keyword :  when the break condition met, then will terminate immediately no further execution.
for j in range(1, 11):
    if j == 5:
        break
    print(j, end=" ")
# 1 2 3 4

print()
print("_"*50)
###################### program to check prime number ##################
num = 13
prime = True
for i in range(2, num):
    if num%i == 0:
        prime = False
        break
    else:
        continue

if prime:
    print("This is prime number :", num)
else:
    print("This is not a prime number :", num)


print("_"*50)
################################### Nested If condition ################
# for one single value of outer loop entire loop will execute.

for i in range(1, 6):
    print("address i:", i)
    for j in range(1, 4):
        print("package j:", j)
    print("_"*50)


print("_"*50)
###################### while Loop ################
# while loop will execute the code, till specific condition is true
n = 1
while n <= 10:
    print(n)
    n = n+1


print("_"*50)
# infinite loop
n = 1
while True:
    print(n)
    n = n+1
    if n == 100000:
        break


