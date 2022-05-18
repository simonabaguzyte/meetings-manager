import json


def read_json_file(file_name):
    data = []

    file = None
    try:
        file = open(file_name, "r")
        data = json.load(file)
    except FileNotFoundError:
        file = open(file_name, "w")
        data = []
        file.write(json.dumps(data))
    finally:
        file.close()

    return data


def write_json_file(file_name, data):
    json_data = json.dumps(data)

    file = open(file_name, "w")
    file.write(json_data)
    file.close()
