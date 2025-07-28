
"""
range(start value, end value, step value)
->output will include the start value and exclude end value e.g. range (2,5,1): 2,3,4
range(1,10,2):



for i in range(2,7,1):
    print(i)

print('_'*50)

#Print a program to print a table of any number

for i in range(1, 11):
    print(i, "*", 3, "=", i*3)



#Program to get even number from 1 to 85
for i in range(1,85):
    if i%2 ==0:
        print(i)
    else:
        continue

"""

### Apply loop on String####
str1 = "Good Morning"

for char in str1:
    print(char)

#Get vowels from the string

str2 = "Good Morning"
vowels = 'aeiou'
for char in str1:
    if char in vowels:
        print(char)
    else:
        continue