"""
Data Abstraction :  Hiding the internal architecture code and implimentation and show only overview information to the user
Then it is called data abstraction.

In pythod, when we define a method in one class and implement the same method in child class,
  then it is called abstract method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def name(self):
        pass

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

str.upper()