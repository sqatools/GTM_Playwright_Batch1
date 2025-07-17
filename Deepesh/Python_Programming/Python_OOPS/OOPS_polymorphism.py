"""
polymorphism : When one method/operator perform multiple task, then it is called polymorphism.
1. Method overriding : when two classes are connected via inheritance and both the class have method with same name
                       then child class method will override the parent class method.
2. Method overloading : Python does not support method overloading
                       ->  When one class have 2 method with same name and different parameters, then it is called method overloading
                       -> In case of python if we define such scenario, then it will only consider the latest defined method.
3. Operator overloading : When one operator performing multiple task, then it is called operator overloading
                         e.g. plus operator can add 2 integer, or 2 string or 2 list values.
"""


# 1. Single Inheritance
# parent/base class
class Father:
    def __init__(self, f_name, f_car, f_business):
        self.father_name = f_name
        self.father_car = f_car
        self.father_business = f_business

    def show_father_details(self):
        print("Father Name :", self.father_name)
        print("Father Car :", self.father_car)
        print("Father Business :", self.father_business)

    def addition(self, n1, n2):
        print("Addition in Father class:", n1 + n2)


# child/derived class
class Son(Father):
    def __init__(self, son_name, f_name, f_car, f_business):
        super().__init__(f_name, f_car, f_business)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()

    def addition(self, n1, n2, n3):
        print("Addition in son class:", n1 + n2 + n3)


    def multiplication(self, v1, v2):
        print("multiply with 2 variable:", v1*v2)

    def multiplication(self, v1, v2, v3):
        print("multiply with three variable :", v1*v2*v3)


obj = Son('Mohit', 'Anuj Verma', 'BMW', 'Construction')
obj.show_family_details()
obj.addition(40, 50, 60)
obj.multiplication(40, 5, 4)


print("_"*50)
############################ Operator overloading #######################
var1 = 30
var2 = 40
print("addition :", var1+var2)
print("addition :", var1.__add__(var2))
print(dir(int))


print("_"*50)
str1 = "Hello"
str2 = "Good Morning"
print(str1 + str2)
print(str1.__add__(str2))
print(dir(str))

print("_"*50)
l1 = [6, 7, 8]
l2 = [1, 3, 5]
print("add list values :", l1+l2)
print("Add list values :", l1.__add__(l2))
print(dir(list))

