import unittest
from coffee import CoffeeMachine, coffee_choice

class TestCoffeeMachine(unittest.TestCase):
    def test_machine_creation(self):
        m = CoffeeMachine()
        self.assertTrue(m, "Status:\n  Water= 100\n  Coffee= 500\n  Milk= 1000\n")


"""
def test_valid_choice():
    assert coffee_choice() == pass

def test_invalid_choice():
    assert coffee_choice() == pass
"""
