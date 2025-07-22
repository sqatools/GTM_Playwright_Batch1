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

round1 = "fail"
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

######IN Operator########


list1 = [5, 10, 15, 1, 2.1]
if 22 in list1:
    print("that number is available")
else:
    print("that number does not exist")

tup = (3, 4, 5, 8)

if 5 in tup:
    print("number 5 is available ")
else:
    print("number 5 does not exist")


#########NOT Operator#########
dict_id = 'v'
dict_list ={'v': 400, 's': 700, 'j': 350, 'y': 300, 'h': 450}
if dict_id not in dict_list:
    print("add the Dict number in order to view the value")
else:
    print("yes, this dict exist ", dict_list)




#############IS Operator ############
num = 948

if num:
    print("it is the correct num")
else:
    print("this not correct ")
