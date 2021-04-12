from collections import defaultdict
import json

d = defaultdict(list)
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for action in scenes['action']:
                d[action['character']].append(action['says'])
print(d)
