import json

characters = []
with open('json_new.json', 'w', encoding='utf-8') as new_file:
    with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file:
        dict_obj = json.load(file)
        for acts in dict_obj["acts"]:
            for scenes in acts["scenes"]:
                for action in scenes["action"]:
                    if action['character'] not in characters:
                        characters.append(action['character'])
                new_json = json.dumps(characters)
                new_file.write(new_json + '\n')
                characters = []





