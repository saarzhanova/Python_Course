import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open('new.xml', 'w', encoding='utf-8') as file:
    for source in root.iter('source'):
        file.write(source.text + '\n')
print('Done!')


