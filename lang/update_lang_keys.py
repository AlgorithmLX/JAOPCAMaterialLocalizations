import json
import os

dirname = os.path.dirname(__file__)

name = input("Lang file: ")

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
        material = material.strip().split(" ", 2)[0].strip()
        if material:
            key = "jaopca.material."+material
            if key not in lang:
                lang[key] = ""

with open(lang_filename, "w", encoding="utf-8") as lang_file:
    json.dump(lang, lang_file, ensure_ascii=False, indent="\t", sort_keys=True)
