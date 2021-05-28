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
        self._sentence = sentence[0].text
        self._wordforms = []
        for token in sentence.iter('token'):
            wf = WordForm(token)
            self._wordforms.append(wf)

    def get_wf(self, num):
        if num < len(self._wordforms):
            return self._wordforms[num]

    def get_text(self):
        print(self._sentence)
        return self._sentence


class WordForm:
    def __init__(self, wordform):
        self._wordform = wordform.get('text')
        self._grammemes = []
        for item in wordform.iter('g'):
            self._grammemes.append(item.get('v'))

    def get_gr(self, num):
        if num < len(self._grammemes):
            return self._grammemes[num]

    def get_text(self):
        print(self._wordform)
        return self._wordform


corp = Corpus()
corp.load_corp('annot.opcorpora.no_ambig.xml')
s = corp.sentences(7)
wf = s.get_wf(1)
gr = wf.get_gr(0)
s.get_text()
wf.get_text()
print(gr)