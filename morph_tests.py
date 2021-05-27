from morph_1 import corp, Corpus, s, Sentence, wf, WordForm, gr
import unittest


class CorporaTester(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(isinstance(corp, Corpus))
        self.assertTrue(isinstance(s, Sentence))
        self.assertTrue(isinstance(wf, WordForm))
        self.assertTrue(isinstance(gr, str))

    def test_outtxt(self):
        self.assertTrue(isinstance(s.text(), str))
        self.assertTrue(isinstance(wf.text(), str))

    def test_formtxt(self):
        self.assertIn(wf.text(), s.text())

    def test_insides(self):
        self.assertEqual(s.text(), 'Потом проект переехал с «Культуры» на НТВ.')
        self.assertEqual(wf.text(), 'проект')
        self.assertEqual(gr, 'NOUN')


if __name__ == '__main__':
    unittest.main()
