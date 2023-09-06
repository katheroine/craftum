import unittest
from rubber_duck import RubberDuck
import sys
from io import StringIO

class TestRubberDuck(unittest.TestCase):
    def test(self):
        duck = RubberDuck()
        self.assertIsInstance(duck, RubberDuck)

    def test_get_species(self):
        expected_species = "-"
        duck = RubberDuck()
        actual_species = duck.get_species()
        self.assertEqual(actual_species, expected_species)

    def test_quack(self):
        duck = RubberDuck()
        output = StringIO()
        sys.stdout = output
        duck.quack()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "Squeak!\n")

    def test_fly(self):
        duck = RubberDuck()
        output = StringIO()
        sys.stdout = output
        duck.fly()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "")


if __name__ == '__main__':
    unittest.main()
