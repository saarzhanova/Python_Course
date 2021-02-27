import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open('new.xml', 'w', encoding='utf-8') as file:
    for text in root.findall('text'):
        for paragraphs in text.findall('paragraphs'):
            for paragraph in paragraphs.findall('paragraph'):
                for sentence in paragraph.findall('sentence'):
                    source = sentence.find('source').text
                    file.write(source + '\n')


