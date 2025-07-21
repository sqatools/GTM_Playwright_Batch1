"""
Date: 18th july 2025
Data hiding/encapsulation : when we want to restrict the access of data outside of the class and bind the class member
in one single unit then it is called data hiding.

"""

class Car:
    def __init__(self,car_name,car_price,car_comp):
        self.car_name= car_name
        self._car_price=car_price
        self.__car_company=car_comp

    # Public member
    def show_car_name(self):
        print("Car Name:", self.car_name)

    # Protected member
    def _show_car_price(self):
        print("Car Price:",self._car_price)

    # Private member
    def __show_car_company(self):
        print("Car Company:",self.__car_company)

obj=Car('Harrier','20 Lakh','Tata')
# Access public member
obj.show_car_name()

# 1. when we define any variable or method with single underscore as prefix, then those class members will
#    not show in suggestion list.

# Access protected member
# Access the class member with single underscore as prefix
obj._show_car_price()


# Access private member
# Access the class member with double underscore as prefix
# e.g. _classname__variable/method name.

obj._Car__show_car_company()