import unittest
from task1 import substract, check_in, check_grater, check_count

class TestNumbers(unittest.TestCase):

    def test_true(self):
        self.assertTrue(substract(10, 5))

    def test_false(self):
        self.assertFalse(substract(5, 10))

    def test_in(self):
        c, d = check_in(15, 10)
        self.assertIn(c, d)

    def test_notin(self):
        c, d = check_in(10,15)
        self.assertNotIn(c,d)

    def test_greater(self):
        self.assertGreater(check_grater(100,20),100)

    def test_less(self):
        self.assertLess(check_grater(100,20),500)

    def test_count(self):
        c, d = check_count(10,15)
        self.assertCountEqual(c,d)


if __name__ == '__main__':
    unittest.main()