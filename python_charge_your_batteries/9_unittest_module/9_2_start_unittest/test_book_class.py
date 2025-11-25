import unittest
from .example_methods import Book


class TestBookClass(unittest.TestCase):
    def test_init_method(self):
        try:
            book = Book('T', 'A', 45, 1)
        except TypeError:
            self.fail()


    def test__str__method(self):
        book = Book('T', 'A', 45, 1)
        self.assertEqual('T by A', str(book))

    def test_get_reading_time(self):
        book = Book('T', 'A', 10, 1)
        result = book.get_reading_time()
        self.assertEqual(result, '15.0 minutes')

    def test_apply_discount_not_float(self):
        book = Book('T', 'A', 10, 1)
        with self.assertRaises(ValueError):
            book.apply_discount(1)

    def test_apply_discount_more_than_1(self):
        book = Book('T', 'A', 10, 1)
        with self.assertRaises(ValueError):
            book.apply_discount(2)

    def test_apply_discount_less_than_0(self):
        book = Book('T', 'A', 10, 1)
        with self.assertRaises(ValueError):
            book.apply_discount(-1)

    def test_apply_discount_good_case(self):
        book = Book('T', 'A', 10, 10)
        result = book.apply_discount(0.5)
        self.assertEqual(result, '$5.0')