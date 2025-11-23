import unittest
from .check_list import is_sorted_ascending, is_sorted_descending


class CheckListTestCase(unittest.TestCase):

    def test_list_is_ascending(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(is_sorted_ascending(lst))

    def test_list_is_not_ascending(self):
        lst = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
        self.assertFalse(is_sorted_ascending(lst))

    def test_list_is_descending(self):
        lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertTrue(is_sorted_descending(lst))

    def test_list_is_not_descending(self):
        lst = [10, 9, 8, 7, 6, 5, 4, 3, 1, 2]
        self.assertFalse(is_sorted_descending(lst))


if __name__ == '__main__':
    unittest.main()
