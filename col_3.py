from collections import Counter
import json

b = []
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for action in scenes['action']:
                b.append(action['character'])
c = Counter()
for character in b:
    c[character] += 1
print(c)