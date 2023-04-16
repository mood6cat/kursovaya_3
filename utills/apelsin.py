import json


def load_files(files):
    with open("operations.json", 'r', encoding="utf-8") as f:
        files = json.load(f)
    print(files)




