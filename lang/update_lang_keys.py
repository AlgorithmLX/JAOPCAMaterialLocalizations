import json
import os
import unicodedata

# Modified from StringUtils.splitByCharacterTypeCamelCase in Apache Commons Lang
def split_by_character_type_camel_case(string: str):
    if not string:
        return ""
    ret = []
    token_start = 0
    current_category = unicodedata.category(string[token_start])
    for pos in range(1, len(string)):
        category = unicodedata.category(string[pos])
        if category == current_category:
            continue
        if category == "Ll" and current_category == "Lu":
            new_token_start = pos - 1
            if new_token_start != token_start:
                ret.append(string[token_start:new_token_start])
                token_start = new_token_start
        else:
            ret.append(string[token_start:pos])
            token_start = pos
        current_category = category
    ret.append(string[token_start:])
    return " ".join(ret)

dirname = os.path.dirname(__file__)

name = input("Lang file: ")

with open(os.path.join(dirname, "en_us.json"), "r", encoding="utf-8") as lang_file:
    default_lang = json.load(lang_file)

lang_filename = os.path.join(dirname, name+".json")
lang = dict()

if os.path.isfile(lang_filename):
    with open(lang_filename, "r", encoding="utf-8") as lang_file:
        try:
            lang = json.load(lang_file)
        except json.JSONDecodeError:
            pass

with open(os.path.join(dirname, "materials.txt"), "r", encoding="utf-8") as materials_file:
    for material in materials_file:
        material = material.strip()
        if material:
            key = "jaopca.material."+material
            if key not in lang:
                if key in default_lang:
                    lang[key] = default_lang[key]
                else:
                    lang[key] = split_by_character_type_camel_case(material)

with open(lang_filename, "w", encoding="utf-8") as lang_file:
    json.dump(lang, lang_file, ensure_ascii=False, indent="\t", sort_keys=True)
