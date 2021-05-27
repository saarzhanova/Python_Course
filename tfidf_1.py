import xml.etree.ElementTree as ET
import re
import json
import collections
import math
import os.path


class Texts:

    def __init__(self, path_to_corpus):
        self._texts = []
        tree = ET.parse(path_to_corpus)
        root = tree.getroot()
        for text in root.iter('text'):
            sent = []
            for source in text.iter('source'):
                sent.append(source.text)
            for i in sent:
                self._texts.append(re.sub(r'[^\w\s]', '', i.lower()))
        self.f = open('idf.json', 'r', encoding='utf-8')

    def tf_idf(self, text, corpus):
        tf_idf = []
        tf = []
        idf = {}
        text = text.split()
        _tf_txt = collections.Counter(text)
        for item in _tf_txt:
            tf.append((item, _tf_txt[item] / len(text)))

        if os.path.isfile('idf.json'):
            idf = json.load(self.f)
        else:
            words = str(corpus)
            words = set(re.sub(r'[^\w\s]', '', words).split())
            a = 0
            for i in words:
                for text in corpus:
                    if i in text:
                        a += 1
                if a != 0:
                    idf[i] = math.log10(len(corpus) / a)
            self.f.write(json.dumps(idf))
        for i in tf:
            tf_idf.append((i[0], i[1]*idf.get(i[0])))
        return tf_idf

    def get_text(self, num):
        if num < len(self._texts):
            return self._texts[num]

    def get_corpus(self):
        return self._texts


text = Texts('annot.opcorpora.no_ambig.xml')
print(text.get_text(10))
print(text.tf_idf(text.get_text(10), text.get_corpus()))