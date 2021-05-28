from collections import Counter
import json


c = Counter()
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for action in scenes['action']:
                reply = ' '.join(action['says'])
                reply = reply.split(' ')
                c.update(reply)
print(c.most_common(20))
print(c.most_common()[:-21:-1])