from abc import ABC, abstractmethod
import random


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


class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 20)


class Potato(Plant):
    def __init__(self):
        super().__init__("Potato", 15)


class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot", 10)


class Animal(Purchaseable):
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

    def buy(self):
        print(f"Bought a {self.name} for ${self.cost}")

    @abstractmethod
    def interact(self):
        pass


class Cow(Animal):
    def __init__(self):
        self.name = "Cow"
        self.cost = 50

    def interact(self):
        print("Milked the cow. You got fresh milk!")


class Chicken(Animal):
    def __init__(self):
        self.name = "Chicken"
        self.cost = 30

    def interact(self):
        print("Collected eggs from the chicken. You got fresh eggs!")


class Cat(Animal):
    def __init__(self):
        self.name = "Cat"
        self.cost = 40

    def interact(self):
        print("You petted the cat!")


class ItemFactory:
    def __init__(self):
        pass

    def get_available_items(self):
        return {
            "1": Tomato(),
            "2": Potato(),
            "3": Carrot(),
        }

    def enhance_seeds(self, item):
        item.resell_value *= 2
        item.name = f"Rare {item.name}"

        def buy():
            print(f"Bought {item.name} seeds for ${item.cost}. These sell for more!")

        item.buy = buy

    def create_item(self, item_type):
        item = self._create_item_object(item_type)
        if random.choice([True, False]):
            self.enhance_seeds(item)
        return item

    def _create_item_object(self, item_type):
        if item_type == "Tomato":
            return Tomato()
        elif item_type == "Potato":
            return Potato()
        elif item_type == "Carrot":
            return Carrot()
        else:
            raise ValueError("Invalid item type")

    def parse_names(self, names):
        items = []
        if names == [] or names[0] == "":
            return items

        for name in names:
            if "Rare" in name:
                item_name = name.split()[1]
                item = self._create_item_object(item_name)
                self.enhance_seeds(item)

            else:
                item = self._create_item_object(name)

            items.append(item)

        return items


class AnimalFactory:
    def __init__(self):
        pass

    def get_available_animals(self):
        return {
            "1": Cow(),
            "2": Chicken(),
            "3": Cat(),
        }

    def create_animal(self, animal_type):
        if animal_type == "Cow":
            return Cow()
        elif animal_type == "Chicken":
            return Chicken()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

    def parse_names(self, names):
        animals = []
        if names == [] or names[0] == "":
            return animals
            
        for name in names:
            animal = self.create_animal(name)
            animals.append(animal)
        return animals
