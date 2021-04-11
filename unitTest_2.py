import unittest
import random


class TestRands(unittest.TestCase):

    def test_rands(self):
        n = 10
        rands = [random.random() for x in range(n)]
        print(rands)
        for rand in rands:
            with self.subTest(rand=rand):
                self.assertGreaterEqual(rand, 0.5)


if __name__ == '__main__':
    unittest.main()