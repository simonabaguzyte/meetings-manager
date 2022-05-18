import json


def load_json_file(file):
    data = None
    try:
        data = json.load(file)
    except json.decoder.JSONDecodeError:
        # TODO: Add incorrect JSON handling here
        pass

    return data


def read_json_file(file_name):
    file = None
    try:
        file = open(file_name, "r")
        return load_json_file(file)
    except FileNotFoundError:
        data = json.dumps([])
        file = open(file_name, "w")
        file.write(data)
        return []
    finally:
        file.close()


def add_to_json_file(file_name, data_dict):
    file_array = read_json_file(file_name)
    file_array.append(data_dict)

    new_json = json.dumps(file_array)
    file = open(file_name, "w")
    file.write(new_json)
    file.close()
    