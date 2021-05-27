import unittest
from tfidf_1 import Texts

text = Texts('annot.opcorpora.no_ambig.xml')


class Tests(unittest.TestCase):
    def test_tf_idf(self):
        a = text.tf_idf(text.get_text(10), text.get_corpus())
        b = [('народные', 1.995568717560156), ('любимцы', 1.995568717560156)]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()