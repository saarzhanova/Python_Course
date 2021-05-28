from morph_1 import Corpus, Sentence, WordForm
import unittest


class TestCorpora(unittest.TestCase):
    def setUp(self):
        self.corp = Corpus()
        self.corp.load_corp('annot.opcorpora.no_ambig.xml')
        self.sentence = self.corp.sentences(7)
        self.wordform = self.sentence.get_wf(1)
        self.grammemes = self.wordform.get_gr(0)
        self.s_text = self.sentence.get_text()
        self.w_text = self.wordform.get_text()

    def test_sanity(self):
        self.assertTrue(isinstance(self.corp, Corpus))
        self.assertTrue(isinstance(self.sentence, Sentence))
        self.assertTrue(isinstance(self.wordform, WordForm))
        self.assertTrue(isinstance(self.grammemes, str))

    def test_outtxt(self):
        self.assertTrue(isinstance(self.s_text, str))
        self.assertTrue(isinstance(self.w_text, str))

    def test_formtxt(self):
        self.assertIn(self.w_text, self.s_text)

    def test_insides(self):
        self.assertEqual(self.s_text, 'Потом проект переехал с «Культуры» на НТВ.')
        self.assertEqual(self.w_text, 'проект')
        self.assertEqual(self.grammemes, 'NOUN')


if __name__ == '__main__':
    unittest.main()
