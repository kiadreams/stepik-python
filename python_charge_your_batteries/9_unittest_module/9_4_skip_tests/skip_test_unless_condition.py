import unittest

try:
    import external_module
    EXTERNAL_MODULE_AVAILABLE = True
except ImportError:
    EXTERNAL_MODULE_AVAILABLE = False


class TestWithExternalModule(unittest.TestCase):

    @unittest.skipUnless(EXTERNAL_MODULE_AVAILABLE, "Тест пропущен: external_module не установлен.")
    def test_requires_external_module(self):
        # Тест, который требует наличие external_module
        result = external_module.do_something()
        self.assertTrue(result)

    def test_another_test(self):
        self.assertEqual(2 * 3, 6)


if __name__ == '__main__':
    unittest.main()
