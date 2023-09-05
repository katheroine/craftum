import unittest
from duck import Duck

class TestDuck(unittest.TestCase):
    def test(self):
        duck = Duck("Mallard")
        number = 100
        self.assertIsInstance(duck, Duck)

    def test_get_species(self):
        expected_species = "xyz"
        duck = Duck(expected_species)
        actual_species = duck.get_species()
        self.assertEqual(actual_species, expected_species)


if __name__ == '__main__':
    unittest.main()
