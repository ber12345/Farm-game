# Farm-game
##
### Introduction

<p>The goal of my course work is to create a simple farm game which meets the requirements, shows what i learned over the semester and also to expand my knowledge on python programming. In my farm game you can buy and plant seeds, harvest them for money. With that money you can also buy animals and interact with them. The games progress saves into a text file so if you exit and start it again your progress is still there. The program can be run by runninng it in visual studio code. You use it by typing input in the terminal which makes the program perform actions accordingly.<br>

##
### Body/Analysis
<p>This program has unit tests for its core functions and it can read and write from file<br>
<p>This program includes all 4 object-oriented programming pillars:<br>

<ul>
  <li>Polymorphism</li>
  <li>Abstraction</li>
  <li>Inheritance</li>
  <li>Encapsulation</li>
</ul>

Also it includes a pattern:
<ul>

  <li>Factory method</li>
</ul>


I will go through my implementation of each one of them

#### Polymorphism

<p>
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface or method to be used with objects of various types, providing flexibility and extensibility in code design. For polymorphism I have an example of base class Purchasable and class plant which inherrits from that class and overrides its method 'buy' with their own implementation and also adds a new 'harvest' method. I did it so code is simplified and so class Plant can have their own methods that fit them as shown in the code below:<br>

```
class Purchaseable(ABC):
    def __init__(self, cost):
        self.cost = cost

    @abstractmethod
    def buy(self):
        pass


class Plant(Purchaseable):
    def __init__(self, name, cost):
        self.name = name
        self.resell_value = cost * 2
        self.cost = cost

    def buy(self):
        print(f"Bought {self.name} seeds for ${self.cost}")

    def harvest(self):
        print(f"Harvested {self.name} and earned ${self.resell_value}")
```
#### Abstraction
<p>
Abstraction in programming is the process of hiding complex implementation details and exposing only the essential features of an object or system. It works by defining a clear and simplified interface that hides the complexities of how things work internally. In the same code snippet we have an example of abstraction. There is an abstract method 'buy' in the base class Purchaseable with a pass. It focuses on what an object does rather than how it achieves it. I used it so i can later reuse the 'buy' method in the code with different methods.<br>

#### Inheritance
<p>
Inheritance allows a new class (subclass or derived class) to inherit attributes and methods from an existing class (superclass or base class). It enables code reuse and promotes the creation of hierarchical relationships between classes.It's also used in the code above where Plant inherits from Purchaseable class. I also used enheritance more in the application like Tomoto inheriting from Plant (as shown in the code below) so I don't have to rewrite code and I can assign values. Inheretence is also used for Animal class in my code which inherits from Purchaseables also as well as seperate animals inhereting from the class Animals<br>

```
class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 20)
```

#### Encapsulation
<p>Encapsulation refers to the bundling of data (variables) and methods (functions) that operate on the data into a single unit called an object. It also involves restricting direct access to some of an object's components, which is a means of preventing accidental interference and misuse of the data. I use encapsulation in my code to make some attributes protected. So that attributes and methods can be accessed within the class and its subclasses. For example. A protected method that can be accessed within the ItemFactory class as shown in the code below:<br>

```
    def _create_item_object(self, item_type):
        if item_type == "Tomato":
            return Tomato()
        elif item_type == "Potato":
            return Potato()
        elif item_type == "Carrot":
            return Carrot()
        else:
            raise ValueError("Invalid item type")
```
Also money attribute in class Player:

```
class Player:
    def __init__(self, money, item_names, animal_names):
        self._money = money
        self.inventory = item_factory.parse_names(item_names)
        self.owned_animals = animal_factory.parse_names(animal_names)
```

#### Factory method

<p>The Factory Method pattern is used in the provided code to create instances of items and animals in a structured and extensible manner. This design pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. The Factory Method pattern is most suitable in this scenerio, because it encapsulates object creation, supports polymorphic creation of objects, and makes it easy to extend the system with new types of items and animals. Other patterns either add unnecessary complexity or do not provide the same level of flexibility in managing object creation.<br>

#
### Results
<ul>
  <li>Made a simple farm game which can be played using user input</li>
  <li>The game can show how much of each item you have in your inventory</li>
  <li>Made many improvements to the code over time. At first it wasn't possible to buy multiples also sell multiples of items and now its possible</li>
  <li>The progress saves correctly which at first didn't</li>
</ul>

#
### Conclusions 
<p>While doing this coursework I learned new things like factory method pattern, how to do unit testing and how to write and read from files. This application became a simple game about farming with relatively limited game functions which still were hard to code right, but after a while everything worked. This application could be extended by adding more plants and animals, also adding more functions like watering the plants for them to grow or actually earning money from interacting with animals. Also days could be added so your plants take a certain amount of days to grow and you pass the days by sleeping. But it would be too difficult for me to code as of now so this program is what i have.<br>
