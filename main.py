import os
from enum import Enum
from items import (
    Animal,
    AnimalFactory,
    ItemFactory,
    Plant,
)


item_factory = ItemFactory()
animal_factory = AnimalFactory()


class MenuChoice(Enum):
    BUY_SEED = "1"
    HARVEST_CROPS = "2"
    BUY_ANIMAL = "3"
    INTERACT_ANIMAL = "4"
    CHECK_INVENTORY = "5"
    CHECK_MONEY = "6"
    EXIT = "7"


class Player:
    def __init__(self, money, item_names, animal_names):
        self._money = money

        self.inventory = item_factory.parse_names(item_names)
        self.owned_animals = animal_factory.parse_names(animal_names)

    def buy(self, purchaseable):
        if self._money >= purchaseable.cost:
            purchaseable.buy()
            self._money -= purchaseable.cost
            if isinstance(purchaseable, Plant):
                self.inventory.append(purchaseable)
            elif isinstance(purchaseable, Animal):
                self.owned_animals.append(purchaseable)
        else:
            print("Insufficient funds!")

    def interact_with_animals(self):
        if self.owned_animals:
            print("\nInteracting with animals:")

            for animal in self.owned_animals:
                animal.interact()
        else:
            print("\nYou don't have any animals to interact with!")

    def harvest_crops(self):
        total_earnings = 0
        for plant in self.inventory:
            plant.harvest()
            total_earnings += plant.resell_value

        self.inventory.clear()
        print(f"\nTotal Earnings: ${total_earnings}")
        self._money += total_earnings

    def play(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n===== Farm Menu =====")
            print("1. Buy and plant a seed")
            print("2. Harvest Crops")
            print("3. Buy Animals")
            print("4. Interact with Animals")
            print("5. Check Inventory")
            print("6. Check Money")
            print("7. Exit")

            try:
                user_input = input("\nEnter your choice: ")
                choice = MenuChoice(user_input)
            except ValueError:
                input("\nInvalid choice!\nClick Enter to continue...")
                continue

            match choice:
                case MenuChoice.BUY_SEED:
                    available_items = item_factory.get_available_items()

                    for index, plant in available_items.items():
                        print(f"{index}. {plant.name} (Cost: ${plant.cost})")

                    choice = input("Enter the plant number you want to buy: ")
                    try:
                        plant = item_factory.create_item(available_items[choice].name)
                    except (IndexError, ValueError):
                        print("Invalid choice!")
                    self.buy(plant)

                case MenuChoice.HARVEST_CROPS:
                    self.harvest_crops()

                case MenuChoice.BUY_ANIMAL:
                    available_animals = animal_factory.get_available_animals()

                    for index, animal in available_animals.items():
                        print(f"{index}. {animal.name} (Cost: ${animal.cost})")

                    choice = input("Enter the animal number you want to buy: ")
                    try:
                        item = animal_factory.create_animal(
                            available_animals[choice].name
                        )
                    except (IndexError, ValueError):
                        print("Invalid choice!")

                    self.buy(item)

                case MenuChoice.INTERACT_ANIMAL:
                    self.interact_with_animals()

                case MenuChoice.CHECK_INVENTORY:
                    if len(self.inventory) == 0:
                        print("Your inventory is empty!")
                    else:
                        print("\nInventory:")
                        item_counts = {}
                        for item in self.inventory:
                            item_counts[item.name] = item_counts.get(item.name, 0) + 1
                        for item, count in item_counts.items():
                            print(f"{item}: {count}")

                case MenuChoice.CHECK_MONEY:
                    print(f"\nCurrent Money: ${self._money}")

                case MenuChoice.EXIT:
                    print("Exiting the game...")
                    break

            input("\nClick Enter to continue...")

    def save_progress(self):
        with open("progress.txt", "w") as file:
            file.write(f"{self._money}\n")
            file.write(",".join([item.name for item in self.inventory]) + "\n")
            file.write(",".join([animal.name for animal in self.owned_animals]) + "\n")


if __name__ == "__main__":
    try:
        with open("progress.txt", "r") as file:
            money = int(file.readline())
            inventory = file.readline().strip().split(",")
            owned_animals = file.readline().strip().split(",")
    except FileNotFoundError:
        money = 100
        inventory = []
        owned_animals = []

    player = Player(money, inventory, owned_animals)
    player.play()
    player.save_progress()