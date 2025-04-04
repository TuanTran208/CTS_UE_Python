import os
import json


def get_default_cfg():
    return os.path.join(os.path.dirname(__file__), "config_files", "mannequin.json")


def readJson(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            print("Load json file {}".format(path))
            dct = json.load(f)
            print(dct)
            return dct

    return None


def saveJson(data, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(data, f, indent=2, separators=[",", ":"])
        print("Save json file {}".format(path))
