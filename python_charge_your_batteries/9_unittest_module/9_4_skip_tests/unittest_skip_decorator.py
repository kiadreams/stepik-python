import unittest


class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skip('The test is not ready yet')
    def test_case_2(self):
        self.assertEqual(2 * 5, 3)

    def test_case_3(self):
        self.assertEqual(2 * 10, 20)


if __name__ == '__main__':
    unittest.main()
