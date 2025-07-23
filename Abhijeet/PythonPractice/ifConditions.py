
#Check even number is even or odd

Num1 = 11

if Num1%2 ==0:
    print("Num1 is even")

else:
    print("Num1 is odd")


# Write a python program to check given number is divisible by 3 and 5
num2 = 25

if num2%3 ==0 and num2%5 ==0:
    print("Num2 is divisible by 3 and 5")

else:
    print(("num2 is not divisible by 3 and 5"))

# check for or condition

if num2%3 == 0 or num2%5 == 0:
    print("Num2 is divisible by 3 or 5")
else:
    print("Num2 is not divisible by 3 or 5")

# if elif condition
a = 10
b = 20
c = 30

print('_'*84)
if a>b and a>c:
    print(" A is greater number")
elif b>a and b>c:
    print("B is greater number ")
elif c>a and c>b:
    print("c is greater number")

print('_'*50)
round1 = "Pass"
round2 = "Pass"
round3 = "Pass"
if round1 == "Pass":
    print("Round 1 is cleared")
    if round2 == "Pass":
        print("Round 2 is cleared")
        if round3 == "Pass":
            print("Congrats you have cleared round 3")
        else:
            print("Round 3 not cleared")

    else:
        print("Round 2 is not cleared")
else:
    print("Round 1 is not cleared")


