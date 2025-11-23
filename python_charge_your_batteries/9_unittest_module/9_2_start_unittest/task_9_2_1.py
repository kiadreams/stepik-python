import unittest


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class PrimeNumberTestCase(unittest.TestCase):
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for number in prime_numbers:
            self.assertTrue(is_prime(number))

    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 15, 14, 16, 18, 20, 22, 24, 25, 26]
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number))


if __name__ == '__main__':
    unittest.main()