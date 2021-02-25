import json
from collections import OrderedDict


def read_json_file(fn, ordered=False):
    # read file
    with open(fn, "r") as f:
        data = f.read()

    if ordered:
        return json.loads(data, object_pairs_hook=OrderedDict)

    # parse file
    return json.loads(data)


def write_to_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()
