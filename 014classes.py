from abc import ABC, abstractmethod


class Point:
    # class level attribite
    # common to all objects
    # can be modified with Point.default_color
    # once changed affects all objects
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # to create class factory
    # ease the class creation when certain arguments are common for different objects
    # classmethod, __add__ is a magic method
    @classmethod
    def zero(cls):
        return cls(0,0)   

    def __add__(self, other):
        return self.x+self.y+other.x+other.y

    def draw(self):
        print("Drawing point")
        print(f"Point ({self.x}, {self.y})")

point = Point(5,7)
point.z = 10
# print(type(point))
# print(isinstance(point, Point))
# print(isinstance(point, int))
# print(point.x)


#factory method class creation
point1 = Point.zero()
point1.draw()

# by default obj1 !== obj2 since they have different memory address

print("Adding object value", point + point1)


#-------------------------------------------------------------------------------------

# Inheritance

class Animal:
    def __init__(self):
        self.age = 5
    def eat(self):
        print("eat")

class Mamal(Animal):
    def __init__(self):
        # super prevents method overriding
        super().__init__()
        self.legs = 2

    def walk(self):
        print("walk")

m = Mamal()
print(m.age)
print(m.legs)
m.eat()
m.walk()
print(isinstance(m, Animal))
print(issubclass(Mamal, Animal))


# Multiple inheritance

class Person:
    def greet(self):
        print("person greets")

class Employee:
    def greet(self):
        print("Employee greets")

# First class gets priority
class Manager(Employee, Person):
    pass

m = Manager()
m.greet()


# best way create classes based on property and not classification
# i.e. swim, walk etc. rather then person, animal, mamal...


#-----------------------------------------------------------------------------

# Example of inheritance 

class InvalidOperationError(Exception):
    def __init__(self):
        pass

# To ensure that the the stream is not direcltly used and read is implemented in each sub-class
# we use abstract base class method
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened= True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened= False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")

