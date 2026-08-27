from unittest import TestCase
from coffee import CoffeeMachine, types_dic, coffee_choice
from coffee import InsufficientError, NegativeError

class TestClasses(TestCase):
    def test_negative_error(self):
        with self.assertRaises(NegativeError):
            coffee_machine_4 = CoffeeMachine(-20, 500, 100)
        with self.assertRaises(NegativeError):
            coffee_machine_5 = CoffeeMachine(0, -5, 100)
        with self.assertRaises(NegativeError):
            coffee_machine_6 = CoffeeMachine(100, 0, -1)
        

    def test_invalid_coffee_type(self):
        coffee_machine_1 = CoffeeMachine()
        coffee_type = 'not'
        
        with self.assertRaises(ValueError):
            coffee_machine_1.make_coffee(coffee_type)
    
    def test_make_coffee_good(self):
        coffee_machine_1 = CoffeeMachine()
        coffee_type = 'cold brew'

        coffee_machine_1.make_coffee(coffee_type)

        self.assertEqual(coffee_machine_1.water, 90)
        self.assertEqual(coffee_machine_1.coffee, 420)
        self.assertEqual(coffee_machine_1.milk, 800)

    def test_ingredients_dont_change_if_insufficient(self):
        coffee_machine_2 = CoffeeMachine(50, 50, 0)
        coffee_type = 'latte'

        self.assertEqual(coffee_machine_2.water, 50)
        self.assertEqual(coffee_machine_2.coffee, 50)
        self.assertEqual(coffee_machine_2.milk, 0)
    
    def test_insufficient_error(self):
        coffee_machine_3 = CoffeeMachine(0, 0, 0)
        coffee_type = 'cafe au lait'

        with self.assertRaises(InsufficientError):
            coffee_machine_3.make_coffee(coffee_type)
        
        
if __name__ == "__main__":
    unittest.main()
