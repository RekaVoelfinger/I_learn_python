from src.coffee_machine.CoffeeIngredients import CoffeeIngredients
from src.coffee_machine.Coffee import Coffee


class CoffeeMachine:
    def __init__(self):
        self._ingredients = CoffeeIngredients(400, 540, 120)
        self._cups = 9
        self._money = 550
        self._espresso = Coffee(CoffeeIngredients(water_in_ml=250, milk_in_ml=0, coffee_beans_in_gramm=16), 4)
        self._latte = Coffee(CoffeeIngredients(water_in_ml=350, milk_in_ml=75, coffee_beans_in_gramm=20), 7)
        self._cappuccino = Coffee(CoffeeIngredients(water_in_ml=200, milk_in_ml=100, coffee_beans_in_gramm=12), 6)

    def _has_cup(self):
        can_make_coffee = True
        if self._cups < 1:
            print("Sorry, not enough disposable cup!")
            can_make_coffee = False
        return can_make_coffee

    def _can_make_coffee(self, coffee_ingredients):
        return self._ingredients.has_enough(coffee_ingredients) and self._has_cup()

    # Modify the content of the coffee machine
    def _make_coffee(self, coffee):
        if self._can_make_coffee(coffee.get_ingredients()):
            print("I have enough resources, making you a coffee!")
            self._ingredients._water_in_ml -= coffee.get_ingredients()._water_in_ml
            self._ingredients._milk_in_ml -= coffee.get_ingredients()._milk_in_ml
            self._ingredients._coffee_beans_in_gramm -= coffee.get_ingredients()._coffee_beans_in_gramm
            self._money += coffee.get_price()
            self._cups -= 1

    def _buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
        if coffee_type == "1":
            self._make_coffee(self._espresso)
        if coffee_type == "2":
            self._make_coffee(self._latte)
        if coffee_type == "3":
            self._make_coffee(self._cappuccino)
        else:
            print(f"Invalid option: {coffee_type}")

    def _fill(self):
        """Filling up the coffee machine and modifying its content"""
        self._ingredients._water_in_ml += int(input("Write how many ml of water do you want to add:\n> "))
        self._ingredients._milk_in_ml += int(input("Write how many ml of milk do you want to add:\n> "))
        self._ingredients._coffee_beans_in_gramm += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self._cups += int(input("Write how many disposable cups do you want to add:\n> "))

    def _take(self):
        """Takes the money out from the coffee machine"""
        print(f"I gave you ${self._money}")
        self._money = 0

    def _show_main_menu(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n> ")
        if action == "buy":
            self._buy()
        elif action == "fill":
            self._fill()
        elif action == "take":
            self._take()
        elif action == "remaining":
            print(self._to_string())
        elif action == "exit":
            self._stop()
        else:
            print(f"Invalid action: {action}")

    def _to_string(self):
        """Prints the amount of water, milk etc. in the machine."""
        print("The coffee machine has:")
        print(f"{self._ingredients.to_string()}{self._cups} of disposable cups\n{self._money} USD")

    def _stop(self):
        exit()

    def start(self):
        while True:
            self._show_main_menu()


if __name__ == "__main__":
    cm = CoffeeMachine()
    cm.start()
