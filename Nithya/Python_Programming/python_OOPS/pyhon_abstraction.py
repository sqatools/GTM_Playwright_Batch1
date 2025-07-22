"""
Data Abstraction :  Hiding the internal architecture code and implimentation and show only overview information to the user
Then it is called data abstraction.

In python, when we define a method in one class and implement the same method in child class,
  then it is called abstract method.
"""

from abc import ABC, abstractmethod

class Animal(ABC): # class call Animal and we are setting up the inheritance ABC

    @abstractmethod
    def name(self):
        pass # pass means we dont to want to do any implementation of this particular method
            # if you want to achive the concept OOPS concept what you have to do ? you have define one method inside a class
            # implement the same method in one some child class that way you can achieve the
            #data abstraction

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def breed(self):
        pass

class Dog(Animal):

        def name(self):
            print("Tommy")

        def voice(self):
            print("Barking")

        def breed(self):
            print("Germen Shefered")

obj = Dog()
obj.name()

#str.upper()