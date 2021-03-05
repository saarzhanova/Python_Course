import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
conj = 0
verb = 0
with open('new.xml', 'w', encoding='utf-8') as file:
    for tfr in root.iter('tfr'):
        if tfr.get('t').lower() == 'может':
            for g in tfr.iter('g'):
                if g.get('v') == 'CONJ':
                    conj += 1
                elif g.get('v') == 'VERB':
                    verb += 1
print('В корпусе слово “может” встречается как союз ' + str(conj) + ' раз, а как глагол - ' + str(verb) + ' раз')
