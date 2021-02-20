import json

new_dict_obj = {}
characters = []
with open('json_new.json', 'w', encoding='utf-8') as new_file:
    with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file:
        dict_obj = json.load(file)
        for acts in dict_obj["acts"]:
            for scenes in acts["scenes"]:
                for action in scenes["action"]:
                    if action['character'] not in characters:
                        characters.append(action['character'])
                new_dict_obj[scenes["title"]] = characters
                characters = []
    json.dump(new_dict_obj, new_file, indent=4, ensure_ascii=False)


