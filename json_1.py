import json

new_dict_obj = {}
with open('json_new.json', 'w', encoding='utf-8') as new_file:
    with open('wikidata_1000.json', 'r', encoding='utf-8') as file:
        for item in file:
            dict_obj = json.loads(item)
            try:
                new_dict_obj[dict_obj["label"]["value"]] = dict_obj["description"]["value"]
            except KeyError:
                new_dict_obj[dict_obj["label"]["value"]] = None
    json.dump(new_dict_obj, new_file, indent=4, ensure_ascii=False)