import unittest
from .example_methods import calculate_average


class AverageTestCase(unittest.TestCase):

    def test_empty_list(self):
        result = calculate_average([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = calculate_average(numbers)
        self.assertEqual(result, -3)

    def test_mixed_numbers(self):
        numbers = [1, -2, 3, -4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, 0.6)


if __name__ == '__main__':
    unittest.main()
