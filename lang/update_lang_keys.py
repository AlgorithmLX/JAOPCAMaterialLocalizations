import json
import os

def split_and_capitalize(string: str):
    if not string:
        return ""
    ret = [s.capitalize() for s in string.split("_")]
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
                    lang[key] = split_and_capitalize(material)

with open(lang_filename, "w", encoding="utf-8") as lang_file:
    json.dump(lang, lang_file, ensure_ascii=False, indent="\t", sort_keys=True)
