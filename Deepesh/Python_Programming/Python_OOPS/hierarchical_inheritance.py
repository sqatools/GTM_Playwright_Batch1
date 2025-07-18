"""
Inheritance :  When one class aquire the property of another class, then it is called inheritance
1. Single Inheritance :  class A ->  class B
2. Multi level inheritance :  class A ->  class B ->  class C
3. Multiple Inheritance :  class A ->  class B, class C -> class B
4. Hierarchical Inheritance :  class A -> class B,  class A -> class C
"""

# Hierarchical Inheritance :  class A -> class B,  class A -> class C
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


# child/derived class
class Son1(Father):
    def __init__(self, son_name, f_name, f_car, f_business):
        super().__init__(f_name, f_car, f_business)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()


class Son2(Father):
    def __init__(self, son_name, f_name, f_car, f_business):
        super().__init__(f_name, f_car, f_business)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()


obj = Son1('Mohit', 'Anuj Verma', 'BMW', 'Construction')
obj.show_family_details()

print("_"*50)

obj = Son2('Rahul', 'Anuj Verma', 'BMW', 'Construction')
obj.show_family_details()