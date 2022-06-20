import unittest
import to_test


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(to_test.add(2, 2), 4)

    def test_sub(self):
        self.assertEqual(to_test.sub(8, 4), 4)

    def test_div(self):
        self.assertEqual(to_test.div(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
