import tf-idf_1.py
import unittest


class Tests(unittest.TestCase):
    def test_tf_idf(self):
        a = text.tf_idf('ничуть не бывало', text._texts)
        b = [('ничуть', 1.330379145040104), ('не', 1.330379145040104), ('бывало', 1.330379145040104)]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()