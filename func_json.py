import json


def data_to_json():
    with open('file.json') as file:

        data = json.load(file)
        return data


print(data_to_json())
