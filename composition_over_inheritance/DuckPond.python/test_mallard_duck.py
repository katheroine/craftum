import unittest
from mallard_duck import MallardDuck
import sys
from io import StringIO

class TestMallardDuck(unittest.TestCase):
    def test(self):
        duck = MallardDuck()
        self.assertIsInstance(duck, MallardDuck)

    def test_get_species(self):
        expected_species = "Anas platyrhynchos"
        duck = MallardDuck()
        actual_species = duck.get_species()
        self.assertEqual(actual_species, expected_species)

    def test_quack(self):
        duck = MallardDuck()
        output = StringIO()
        sys.stdout = output
        duck.quack()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "Quack!\n")

    def test_fly(self):
        duck = MallardDuck()
        output = StringIO()
        sys.stdout = output
        duck.fly()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "Weee!\n")


if __name__ == '__main__':
    unittest.main()
