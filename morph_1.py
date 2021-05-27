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
        return self._sentences

    def sentences(self, num):
        if num < len(self._sentences):
            return self._sentences[num]


class Sentence:

    def __init__(self, sentence):
        self._sentence = sentence
        self._wordforms = []
        wfs = []
        for token in self._sentence.iter('token'):
            wf = WordForm(token)
            wfs.append(wf)
        self._wordforms = wfs


    def wordforms(self, num):
            if num < len(self._wordforms):
                   return self._wordforms[num]

    def text(self):
            self._sentsource = self._sentence.find('source').text
            return self._sentsource


class WordForm:

    def __init__(self, wordform):
        self._wordform = wordform
        self._grammemes = []
        for item in self._wordform.iter('g'):
            self._grammemes.append(item.get('v'))

    def grammemes(self, num):
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