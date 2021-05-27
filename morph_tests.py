from morph_1 import Corpus, Sentence, WordForm
import unittest

corp = Corpus()
corp.load_corp('annot.opcorpora.no_ambig.xml')
s = corp.sentences(7)
wf = s.get_wf(1)
gr = wf.get_gr(0)
sentence = s.sentence
wordform = wf.wordform


class CorporaTester(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(isinstance(corp, Corpus))
        self.assertTrue(isinstance(s, Sentence))
        self.assertTrue(isinstance(wf, WordForm))
        self.assertTrue(isinstance(gr, str))

    def test_outtxt(self):
        self.assertTrue(isinstance(sentence, str))
        self.assertTrue(isinstance(wordform, str))

    def test_formtxt(self):
        self.assertIn(wordform, sentence)

    def test_insides(self):
        self.assertEqual(sentence, 'Потом проект переехал с «Культуры» на НТВ.')
        self.assertEqual(wordform, 'проект')
        self.assertEqual(gr, 'NOUN')


if __name__ == '__main__':
    unittest.main()
