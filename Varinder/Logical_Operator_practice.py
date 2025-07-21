# # And operator
# num = 14
# if (num ==10) and (num ==14):
#         print("one condition is true")
# else:
#     print("because both conditions are not true condition gonna fall in else statement")
#
#
# # OR operator
# num1 = 16
# if (num1 == 30) or (num1 == 16):
#     print(" it will print this statement because at lest one condition is true")
# else:
#     print("one statement is false")

#Multiple elif conditions

# grade_result = int(input("enter you grade here :- "))
#
# if 40 < grade_result <= 50:
#     print("your grade is c")
# elif 60 < grade_result <=70:
#     print("you grade is B")
# elif 80< grade_result <=90:
#     print("your grade is A")
# elif 90< grade_result <= 100:
#     print("congratulations your grade is A+")
# else:
#     print("you are failed")



#####Nested IF ELIF condition ######

round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("round one is passed")
    if round2 == "pass":
        print("round 2 is passed")
        if round3 == "pass":
            print("congratulations you passed 3rd round ")
        else:
            print("you failed 3rd round")
    else:
        print("you failed 2nd round ")

else:
    print("round one failed")



