from collections import defaultdict
import json

b = []
d = defaultdict(list)
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for action in scenes['action']:
                a = (action['character'], action['says'])
                b.append(a)
for k, v in b:
    d[k].append(v)
print(d.items())
