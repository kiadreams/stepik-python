import unittest


def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


class TestLinearSearchFunction(unittest.TestCase):

    def test_target_is_exists(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(linear_search(lst, target), 4)

    def test_target_is_not_exists(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(linear_search(lst, target), -1)


if __name__ == '__main__':
    unittest.main()
