import unittest
from duck import Duck
import sys
from io import StringIO

class TestDuck(unittest.TestCase):
    def test(self):
        duck = Duck()
        self.assertIsInstance(duck, Duck)

    def test_get_species(self):
        expected_species = ""
        duck = Duck()
        actual_species = duck.get_species()
        self.assertEqual(actual_species, expected_species)

    def test_quack(self):
        duck = Duck()
        output = StringIO()
        sys.stdout = output
        duck.quack()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "Quack!\n")

    def test_fly(self):
        duck = Duck()
        output = StringIO()
        sys.stdout = output
        duck.fly()
        captured_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output, "Weee!\n")


if __name__ == '__main__':
    unittest.main()
