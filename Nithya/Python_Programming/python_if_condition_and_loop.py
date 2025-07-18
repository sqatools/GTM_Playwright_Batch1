# Check given number is even or odd

num=11

if num%2 == 0:
    print("This is even number")
else:
    print("This is odd number")


"""
cond1 and cond2
True and False :  False
False and True :  False
False and False :  False
True and True :  True

cond1 or cond2:
True or False :  True
False or False :  True
True or True :  True
False or False :  False
"""

# write a python program to check given number is divisible by 3 and 5
num2 = 12
if num2%3 ==0 and num2%5 == 0:
    print("This number is divisible by 3 and 5")
else:
    print("This number is not divisible by 3 and 5")


print("_"*50)
# check program using or condition
num3 = 12
if num3%3 == 11 or num3%5 == 0:
    print("This number is divisible by 11 or 5")
else:
    print("This number is not divisible by 11 or 5")

print('_'*50)
######################################
# If-elif condition :
a=20
b=40
c=60

if a>b and a>c:
    print("a is greater")
if b>a and b>c:
    print('b is greater')
if c>b and c>a:
    print('c is greater')

print("_"*50)
###############################################
# Nested if condition:
"""
if cond1:
   code
   if cond2:
       code
   else:
       code
else:
     else msg
"""

############ Example ###################################
round1='pass'
round2='pass'
round3='fail'

if round1=='pass':
    print('round1 is cleared and go for round2')
    if round2=='pass':
        print('round2 is cleared and gor round3')
        if round=='pass':
            print('round3 is cleared and you get job')
        else:
            print('round3 is not cleared')
    else:
        print('round2 is not cleared')
else:
    print('round2 is not cleared, try next time')

