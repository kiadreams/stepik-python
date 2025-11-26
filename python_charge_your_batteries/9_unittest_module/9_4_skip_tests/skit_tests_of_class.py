import unittest


@unittest.skip('Skip all')
class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertEqual(3 + 1, 5)

    def test_case_3(self):
        self.assertEqual(3 * 7, 21)


if __name__ == '__main__':
    unittest.main()
