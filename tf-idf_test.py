import unittest
from tfidf_1 import Texts


class TestTFIDF(unittest.TestCase):
    def setUp(self):
        self.text = Texts('annot.opcorpora.no_ambig.xml')

    def test_tf_idf(self):
        a = self.text.tf_idf('народные любимцы')
        b = [('народные', 1.7570080902003247), ('любимцы', 1.995568717560156)]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()