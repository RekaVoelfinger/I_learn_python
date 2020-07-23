from unittest import TestCase
from unittest import main
from src.coffee_machine.CoffeeIngredients import CoffeeIngredients
from src.coffee_machine.Coffee import Coffee


class TestCoffee(TestCase):

    def test_constructor(self):
        test_ingredients = CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15)
        test_coffee = Coffee(test_ingredients, 5)
        self.assertIsInstance(test_coffee, Coffee)

    def test_constructor_missing_argument(self):
        test_ingredients = CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15)
        with self.assertRaises(TypeError):
            Coffee(test_ingredients)

    def test_constructor_more_argument(self):
        test_ingredients = CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15)
        with self.assertRaises(TypeError):
            Coffee(test_ingredients,5,5)

    def test_get_ingredients(self):
        expected_ingredients = CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15)
        test_coffee = Coffee(expected_ingredients, 5)
        self.assertEqual(test_coffee.get_ingredients(), expected_ingredients, "Coffee Ingredients")

    def test_get_ingredients_none(self):
        expected_ingredients = CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15)
        test_coffee = Coffee(None, 5)
        self.assertNotEqual(test_coffee.get_ingredients(), expected_ingredients)

    def test_get_ingredients_negative(self):
        expected_ingredients = CoffeeIngredients(water_in_ml=-100, milk_in_ml=150, coffee_beans_in_gramm=15)
        test_coffee = Coffee(expected_ingredients, 5)
        self.assertEqual(test_coffee.get_ingredients(), expected_ingredients)

    def test_get_price(self):
        test_coffee = Coffee(CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15), 5)
        self.assertEqual(test_coffee.get_price(), 5)

    def test_set_price(self):
        test_coffee = Coffee(CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15), 5)
        test_coffee.set_price(1)
        self.assertEqual(test_coffee.get_price(), 1)

    def test_set_price_negative(self):
        test_coffee = Coffee(CoffeeIngredients(water_in_ml=100, milk_in_ml=150, coffee_beans_in_gramm=15), 5)
        #with self.assertRaises(ValueError):
        with self.assertRaises(SyntaxError):
            test_coffee.set_price(-1)

unittest.main(module='test_Coffee', exit=False)

if __name__ == '__main__':
    main(module="test_Coffeee")
