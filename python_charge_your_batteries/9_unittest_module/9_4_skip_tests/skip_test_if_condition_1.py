import unittest

APP_VERSION = "1.0.0"  # Предположим, что текущая версия приложения - 1.0.0


class MyTest(unittest.TestCase):

    @unittest.skipIf(APP_VERSION == "1.0.0", "Тест пропуcкаем для версии 1.0.0")
    def test_some_feature(self):
        result = do_some_stuff()
        self.assertTrue(result)

    def test_another_feature(self):
        self.assertEqual(3 + 4, 7)


if __name__ == '__main__':
    unittest.main()
