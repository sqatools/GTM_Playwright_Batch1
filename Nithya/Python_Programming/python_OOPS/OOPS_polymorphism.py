#Class date:17th 2025

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

# polymorphism :

class Father:
    def __init__(self, f_name, f_car, f_business):
        self.father_name = f_name
        self.father_car = f_car
        self.father_business = f_business

    def show_father_details(self):
        print("Father Name :", self.father_name)
        print("Father Car :", self.father_car)
        print("Father Business :", self.father_business)

    def addition(self,n1,n2):
        print("Addition from Father Class :",n1+n2)

# child/derived class
class Son(Father):
    def __init__(self, son_name, f_name, f_car, f_business):
        super().__init__(f_name, f_car, f_business)
        self.son_name=son_name

    def show_son_name(self):
        print("son_name: ",self.son_name)

    def addition(self, n1,n2,n3):
        print("Addition from son Class :", n1+n2+n3)

    def multiplication(self,v1,v2):
        print("Multiplication :", v1*v2)

    def multiplication(self, v1, v2,v3):
        print("Multiplication :", v1 * v2*v3)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()

obj = Son('Mohit', 'Anuj Verma', 'BMW', 'Construction')
obj.show_family_details()
obj.addition(10,10,10)
#obj.multiplication(10,20) #TypeError: Son.multiplication() missing 1 required positional argument: 'v3'

#obj.addition(10,10,10) Through the object you can call the method from father class
                    # method from the son class but if father class and son class both have the
#                   same method then which method we get a priority ?
#                   son class will get the priority
#                   this is called overiding the son class override the method of  parent class

"""
What is method overloading?
one single class two methods with same name but different parameter is called method overloading
But python does not support method overloading
If you define two method with same name but different args then it will only consider the last method with parameter(eg : three is consider) 
whichever method you define at the last will be consider, here you pass two but its show error third is missing
obj.multiplication(10,20) #TypeError: Son.multiplication() missing 1 required positional argument: 'v3'
"""

print("_"*50)
############################ Operator overloading #######################
var1 = 30
var2 = 40
print("addition :", var1+var2)
print("addition :", var1.__add__(var2))
print(dir(int)) #The same method we are using for addition and we can get the list of all files and folders that
#belong to the magic method called integer

"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', 
'__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', 
'__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', 
'__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
 '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
  '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', 
  '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
   '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 
   'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer',
    'numerator', 'real', 'to_bytes']
    
It will call all methods available in integer 
multiplication -> __mul__
Not equal to  -> '__ne__'
less than equal to   -> __le__
or     ->__or__
greater than   -> __gt__
greater equalto  ->__ge__
"""

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