"""
Inheritance :  When one class aquire the property of another class, then it is called inheritance
1. Single Inheritance :  class A ->  class B
2. Multi level inheritance :  class A ->  class B ->  class C
3. Multiple Inheritance :  class A ->  class B, class C -> class B
4. Hierarchical Inheritance :  class A -> class B,  class A -> class C
"""

# 2.  Multi level inheritance : class A ->  class B ->  class C


class GrandFather:
    def __init__(self,gf_name,gf_property):
        self.gf_name = gf_name
        self.gf_property = gf_property

    def show_grandFather_details(self):
        print("Grand Father Name :", self.gf_name)
        print("Grand Father Property :",self.gf_property)



class Father(GrandFather):
    def __init__(self, f_name, f_car, f_business, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = f_name
        self.father_car = f_car
        self.father_business = f_business

    def show_father_details(self):
        print("Father Name :", self.father_name)
        print("Father Car :", self.father_car)
        print("Father Business :", self.father_business)


# child/derived class
class Son(Father):
    def __init__(self, son_name, f_name, f_car, f_business, gf_name, gf_property):
        super().__init__(f_name, f_car, f_business, gf_name, gf_property)
        self.son_name=son_name

    def show_son_name(self):
        print("son_name: ",self.son_name)

    def show_family_details(self):
        self.show_grandFather_details()
        self.show_father_details()
        self.show_son_name()

obj = Son('Mohit', 'Anuj Verma', 'BMW', 'Construction', 'Dayaram', '200 Acr Land')
obj.show_family_details()