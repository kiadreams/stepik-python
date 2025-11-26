import unittest


class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.skipTest('Not ready')

    def test_case_3(self):
        self.skipTest('Not ready too')


if __name__ == '__main__':
    unittest.main()
