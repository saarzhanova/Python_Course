from collections import Counter
import json

c = Counter()
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for action in scenes['action']:
                c[action['character']] += 1
print(c)