# Object Oriented Programming Tutorial Using Solid Principle

# Types of Solid Principles

# 1 - Single Responsibility Principle (SRP)
# 2 - Open-Closed Principle (OCP)
# 3 - Liskov Substitution Principle (LSP)
# 4 - Interface Segregation Principle (ISP)
# 5 - Dependency Inversion Principle (DSP)

##############################################################################################################

# Single Responsibility Principle

# Definition - A class should have only one reason to change

# Explanation :- This means that class should have one responsibility.
# If a class takes care of more than one task you should separate that class

# Lets Understand With Example

# file_manager_srp.py

from abc import ABC, abstractmethod
from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# So as we seen this class handles read and write method and compress and decompress methods

# So after applying SRP

# file_manager_srp.py


class SRPFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# SO here We can see that we have two smaller classes and each have different Responsibilty

# Examples in Our Project : Django Models, OrgWhatsappTestUtils Class (That Manages Whatsapp)

# Where we can apply - We can apply this principle in org_daily_mis_report (TO make code readable and understandable)


######################################################################################################################

# Open Closed Principle

# Introduced by Bertrand Meyer

# Definition - Software Entities (Classes, modules, functions, etc) Should be open for extension but closed for modification

# Explanation -
# 1- Close for modification :- Once a class is built and in use we can not
# modify its source code or try to avoid source code. Changing existing stable
# code can cause bugs and break existing functionality.

# 2- Open for extension :- We can not not change existing code but we can
# change its behavior or add new functionality

# Used Mechanism for functionality

# 1:- Inheritance : When a new class (Sub Class) is created based on existing class (Superclass)
# eg:-
class Animal:  # Superclass
    def speak(self):
        return "Some sound"


class Dog(Animal):  # Subclass
    def speak(self):
        return "Bark"


# 2:- Interfaces/Abstract Class : in python there is only abstractmethod
# Abstract classes are used when you want to provide some default
# functionality but still require subclasses to implement specific parts.
# eg:-


class Animal(ABC):  # Abstract class
    def eat(self):
        print("This animal eats food.")

    @abstractmethod
    def speak(self):
        pass


class DogNew(Animal):
    def speak(self):
        print("Bark")


# 3:- polymorphism : is the ability of different objects to respond to the
# same method call in a way that is specific to their type
# eg :-
class PDog:
    def speak(self):
        return "Bark"


class PCat:
    def speak(self):
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(PDog())  # Output: Bark
make_animal_speak(PCat())  # Output: Meow


# Note : There are many type of polymorphism can read more about this

TODO in Detail
# 4:- Plugins and Strategy patterns 

# Plugins : Plugin is a modular interchangeable component that adds or extend 
# functionality to a core application without modifying its source code
# eg:- 
# In a text editor, spell-checkers or grammar-checkers can be added as plugins.
# The editor doesn't need to change its core logic — it just loads the plugin dynamically.

# Strategy patterns : 
# The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm 
# at runtime by encapsulating each algorithm in a separate class and making them interchangeable.

# Most common example is Payment Gateway

# 5:- Composition
# Composition is an object-oriented design principle where one 
# class contains a reference to another class, allowing it to reuse its functionality rather than inheriting from it.

# example : - a Car has an Engine

# Promotes code reuse.

# More flexible than inheritance.

# Supports change and extension without modifying existing code.


Open Close Example

# Example

# shapes_ocp.py

# This is Before implementing OCP

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
        
from shapes_ocp import Shape

rectangle = Shape("rectangle", width=10, height=5)
rectangle.calculate_area()
50
circle = Shape("circle", radius=5)
circle.calculate_area()
78.53981633974483

# So here init takes shape_type 

# Two shape type is supported in a class but if we have to add new shape_type
# we have to modify the existing code which is not good

# So after applying OCP

# shapes_ocp.py

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
    
# Using this method we can add new shape anytime and add another method also like circumference or Perimeter


#################################################################################################################################################

# Liskov Substitution Principle

# The Liskov substitution principle (LSP) was introduced by Barbara Liskov at an OOPSLA conference in 1987

# Definition: Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program

# In simpler terms, derived classes must be substitutable for their base classes without altering the expected behavior of the program.
# LSP ensures that a class hierarchy is designed in a way that promotes reusability and reliability.

# shapes_lsp.py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
# shapes_lsp.py
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value

# So in this Code we have defined square a subclass of Rectangle, but it violates LSP because it changes the behavior of the base class.
# Square init takes only one parameter side, but it sets both width and height to the same value.


square = Square(5)
vars(square)
{'width': 5, 'height': 5}

square.width = 7
vars(square)
{'width': 7, 'height': 7}

square.height = 9
vars(square)
{'width': 9, 'height': 9}

# vars(obj) shows you the current state (internal data) of an object. or we can say return dict of the object

After applying LSP

# shapes_lsp.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
################################################################################################################################################

# Interface Segregation Principle

# The interface segregation principle (ISP) comes from the same mind as the single-responsibility principle.

# Definition: Clients should not be forced to depend on interfaces they do not use

# Explanation: This principle states that a class should not be forced to implement methods it does not use.
# Instead of having one large, general-purpose interface, it is better to have several smaller,
# more specific interfaces that are tailored to the needs of different clients.

# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

# In this example, the `Printer` interface forces all classes to implement all methods, even if they don't support them.
# Like `OldPrinter` does not support fax and scan functionality, but it still has to implement those methods, which is not ideal.

# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

# In this example, we have separated the `Printer`, `Fax`, and `Scanner` interfaces.
# Now, `OldPrinter` only implements the `Printer` interface, while `NewPrinter` implements all three interfaces.
# This way, classes only implement the methods they actually use, adhering to the Interface Segregation Principle (ISP).

################################################################################################################################################

# Dependency Inversion Principle

# Definition - Abstractions should not depend upon details. Details should depend upon abstractions.

# High-level and low-level modules should not depend on each other directly.
# Instead, both should depend on an abstraction (e.g., an interface or abstract class).
# The details (implementations) should depend on the abstractions, not the other way around.

class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL database")

class App:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on a low-level module

    def start(self):
        self.database.connect()

# Usage
app = App()
app.start()
# In this example, the `App` class directly depends on the `MySQLDatabase` class, which is a low-level module.
# This creates a tight coupling between the two, making it difficult to change the database implementation without
# modifying the `App` class.

# After applying Dependency Inversion Principle

from abc import ABC, abstractmethod

# High-level abstraction
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# Low-level implementation
class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL database")

# Another possible implementation
class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL database")

# High-level module depending on abstraction
class App:
    def __init__(self, database: Database):
        self.database = database  # Depends on abstraction

    def start(self):
        self.database.connect()

# Usage
mysql = MySQLDatabase()
app = App(mysql)
app.start()

# You can easily switch databases:
postgres = PostgreSQLDatabase()
app2 = App(postgres)
app2.start()
# In this example, the `App` class depends on the `Database` abstraction instead of a specific database implementation.
# This allows you to easily switch between different database implementations without modifying the `App` class.









