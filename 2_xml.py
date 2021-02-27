import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
list = []
with open('new.xml', 'w', encoding='utf-8') as file:
    for tfr in root.iter('tfr'):
        for g in tfr.iter('g'):
            list.append(g.get('v'))
        if 'NOUN' in list and 'plur' in list:
            file.write(tfr.get('t') + '\n')
        list = []
print('Done!')






