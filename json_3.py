import json

new_dict_obj = {}
characters = []
says = []
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file:
    dict_obj = json.load(file)
    for acts in dict_obj["acts"]:
        for scenes in acts["scenes"]:
            for action in scenes["action"]:
                characters.append(action['character'])
                says.append(characters.count(action['character']))
print("У " + characters[says.index(max(says))] + " больше всех реплик (" + str(max(says)) + ")")




