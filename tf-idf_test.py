import unittest
from tfidf_1 import text


class Tests(unittest.TestCase):
    def test_tf_idf(self):
        a = text.tf_idf('народные любимцы', text._texts)
        b = [('народные', 1.995568717560156), ('любимцы', 1.995568717560156)]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()