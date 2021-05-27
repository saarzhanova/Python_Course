import unittest
import xml.etree.ElementTree as ET

class Corpus:

    def __init__(self):
        self._sentences = []

    def load_corp(self, corp_way):
        tree = ET.parse(corp_way)
        root = tree.getroot()
        for item in root.iter('sentence'):
            sent = Sentence(item)
            self._sentences.append(sent)

    def sentences(self, num):
        if num < len(self._sentences):
            return self._sentences[num]


class Sentence:

    def __init__(self, sentence):
        self._sentence = sentence
        self._wordforms = []

    def wordforms(self, num):
            wfs = []
            for token in self._sentence.iter('token'):
                wf = WordForm(token)
                wfs.append(wf)
            self._wordforms = wfs
            # print('There are ' + str(len(self._wordforms)) + ' word forms')
            if num < len(self._wordforms):
                   return self._wordforms[num]

    def text(self):
            self._sentsource = self._sentence.find('source').text
            return self._sentsource


class WordForm:

    def __init__(self, wordform):
        self._wordform = wordform
        self._grammemes = []

    def grammemes(self, num):
        for item in self._wordform.iter('g'):
            self._grammemes.append(item.get('v'))
        # print('There are ' + str(len(self._grammemes)) + ' grammemes')
        if num < len(self._grammemes):
                return self._grammemes[num]

    def text(self):
            self._wftext = self._wordform.get('text')
            return self._wftext


corp = Corpus()
corp.load_corp('annot.opcorpora.no_ambig.xml')
s = corp.sentences(7)
wf = s.wordforms(1)
gr = wf.grammemes(0)

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
