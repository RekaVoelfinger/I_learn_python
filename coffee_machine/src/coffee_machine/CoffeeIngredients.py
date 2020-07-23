# Make the class privat
class CoffeeIngredients:
    def __init__(self, water_in_ml, milk_in_ml, coffee_beans_in_gramm):
        self._water_in_ml = water_in_ml
        self._milk_in_ml = milk_in_ml
        self._coffee_beans_in_gramm = coffee_beans_in_gramm

    def has_enough(self, other):
        has_enough = True

        if self._water_in_ml < other._water_in_ml:
            print("Sorry, not enough water!")
            has_enough = False

        if self._milk_in_ml < other._milk_in_ml:
            print("Sorry, not enough milk!")
            has_enough = False

        if self._coffee_beans_in_gramm < other._milk_in_ml:
            print("Sorry, not enough coffee beans!")
            has_enough = False

        return has_enough

    def to_string(self):
        return f"{self._water_in_ml} ml of water\n{self._milk_in_ml} ml of milk\n{self._coffee_beans_in_gramm} gramm of coffee beans\n"
