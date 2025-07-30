"""
class : class is a blueprint of the object where we define all the properties/attribute/functionality of the object.
object : object is an entity through which we can access all the feature/functionality that we defined inside the class
method : When we write a function inside the class, then it became method.
         There are three type of method:
         1. instance method : when we define any method with self as first parameter then is called is instance method.
         2. class method :  when we define method with @classmethod decorator, then it is called class method
              Example:      @classmethod
                            def show_city_name_with_class(cls):
                                print("Class variable city name :", cls.city)

         3. static method :  when we define any method with @staticmethod decorator, then it is called static method
                             -> static method is associated with class name, no need to create of object the class
                                to access the static method, it is same like function outside the class.


                            # @staticmethod
                            # def get_factorial(num):
                            #     fact = 1
                            #     for i in range(num, 0, -1):
                            #         fact = fact*i # 1*5 = 5| 5*4 = 20 | 20*3 = 60 | 60*2 = 120 | 120*1 = 120
                            #     print(f"factorial of {num} :", fact)
                            #



variables : when we define any variable inside the class, then it is called class member variable
        There are 2 type of variable
        1. instance variable : when we define any variable with self keyword, then it is called instance variable.
                              self.v1 = param1 # instance variable
                              self.v2 = param2 # instance variable

        2. class variable: when we define any variable on class level then it is called class variable.
                            class ABC:
                                 city = "Mumbai"



What is self: Self is nothing but the instance/object of the class being created.
            -> when we call any method with the help of instance of the class, then same instance is the first parameter
               to the method internally, no need to pass it explicitly inplace of self parameter on instance method.

constructor : constructor which initialize the memory for the object, and it by default called during the creation of
              object of the class.
              1. default constructor :
              e.g.
                       def __init__(self):
                            print("----- WELCOME TO ABC CLASS -----")

              2. parametrize constructor: we have to provide value to parameter of constructor, during the creation of
                                          the object of the class
                            def __init__(self, param1, param2):
                                print("----- WELCOME TO ABC CLASS -----")
                                self.v1 = param1 # instance variable
                                self.v2 = param2 # instance variable
"""
# class

class ABC:
    city = "Mumbai" # class variable

    # constructor
    def __init__(self, param1, param2):
        print("----- WELCOME TO ABC CLASS -----")
        self.v1 = param1 # instance variable
        self.v2 = param2 # instance variable


    # instance method
    def greeting(self):
        print("Very Good Morning")

    def addition(self):
        print("Addition value :", self.v1 + self.v2)

    def show_city_name(self):
        print("City name :", self.city)


    @classmethod
    def show_city_name_with_class(cls):
        print("Class variable city name :", cls.city)


    @staticmethod
    def get_factorial(num):
        """
        factorial of 5 : 5*4*3*2*1
        :param num:
        :return:
        """
        fact = 1
        for i in range(num, 0, -1):
            fact = fact*i # 1*5 = 5| 5*4 = 20 | 20*3 = 60 | 60*2 = 120 | 120*1 = 120

        print(f"factorial of {num} :", fact)



# create object of the class
obj = ABC(50, 70)

# access the method with the help of object
#obj.greeting()

# call instance method with the help of class name.
ABC.greeting(obj)

obj.addition()
# Addition value : 120

print("_"*50)
# access class method with object
obj.show_city_name()  # Mumbai
# update class variable value with object, that remain only for object
obj.city = "Pune"
obj.show_city_name()  # Pune


obj.show_city_name_with_class() # Mumbai

# access the static method with object
obj.get_factorial(6) # factorial of 6 : 720

# access the static method with class name
ABC.get_factorial(5) # factorial of 5 : 120
