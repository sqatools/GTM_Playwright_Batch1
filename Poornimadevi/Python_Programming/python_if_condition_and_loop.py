# check given number is even or odd
num1 = 12
print(num1%2 == 0)

if num1%2 == 0:
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
# check program for or condition
num3 = 12
if num3%3 == 11 or num3%5 == 0:
    print("This number is divisible by 11 or 5")
else:
    print("This number is not divisible by 11 or 5")


print("_"*50)
######################################
# If-elif condition :

a = 20
b = 60
c = 40
if a > b and a > c :
    print("A has a greater value")
elif b > a and b >c :
    print("B has a greater value")
elif c > a and c > b:
    print("C has a greater value")


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

round1 = "fail"
round2 = "pass"
round3 = "pass"

if round1  == "pass":
    print("congrats first round is cleared")
    if round2 == "pass":
        print("congrats 2nd round is cleared")
        if round3 == "pass":
            print("congrats 3rd round is cleared")
        else:
            print("Failed in 3rd round, try next time")
    else:
        print("Failed in 2nd round, try next time")
else:
    print("Failed in 1st round, try next time")