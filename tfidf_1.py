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
        if os.path.exists('idf_file'):
            self._idf = self._load_idf()
        else:
            self._idf = self._count_idf()

    def _load_idf(self):
        with open('idf.json', 'r', encoding='utf-8') as f_idf:
            return json.load(f_idf)

    def _count_idf(self):
        idf = {}
        words = str(self._texts)
        words = set(re.sub(r'[^\w\s]', '', words).split())
        for i in words:
            a = 0
            for text in self._texts:
                if i in text:
                    a += 1
            if a != 0:
                idf[i] = math.log10(len(self._texts) / a)
        with open('idf.json', 'w', encoding='utf-8') as f_idf:
            f_idf.write(json.dumps(idf))
        return idf

    def tf_idf(self, text):
        tf_idf = []
        tf = []
        text = text.split()
        _tf_txt = collections.Counter(text)
        for item in _tf_txt:
            tf.append((item, _tf_txt[item] / len(text)))
        for i in tf:
            tf_idf.append((i[0], i[1]*self._idf.get(i[0])))
        return tf_idf

    def get_text(self, num):
        if num < len(self._texts):
            return self._texts[num]


text = Texts('annot.opcorpora.no_ambig.xml')
print(text.get_text(10))
print(text.tf_idf('народные любимцы'))
