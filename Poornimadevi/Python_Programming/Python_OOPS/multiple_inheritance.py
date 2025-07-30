"""
Inheritance :  When one class aquire the property of another class, then it is called inheritance
1. Single Inheritance :  class A ->  class B
2. Multi level inheritance :  class A ->  class B ->  class C
3. Multiple Inheritance :  class A ->  class B, class C -> class B
4. Hierarchical Inheritance :  class A -> class B,  class A -> class C
"""

#  Multiple Inheritance :  class A ->  class B, class C -> class B

class Mother:
    def __init__(self, m_name, m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def show_mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Business :", self.mother_business)

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
class Son(Father, Mother):
    def __init__(self, son_name, f_name, f_car, f_business, m_name='Gouri Verma', m_business='Clothing'):
        super().__init__(f_name, f_car, f_business)
        self.mother_name = m_name
        self.mother_business = m_business
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_name()


obj = Son('Mohit', 'Anuj Verma', 'BMW', 'Construction')
obj.show_family_details()

print("_"*50)
obj2 = Son(m_name='Anjali Verma', m_business='Salon', f_business='Media', f_name='Rahul Verma', son_name='Gourav', f_car='Audi')
obj2.show_family_details()
