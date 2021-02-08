import json

def read_json_file(fn):
    # read file
    with open(fn, 'r') as f:
        data= f.read()

    # parse file
    return json.loads(data)