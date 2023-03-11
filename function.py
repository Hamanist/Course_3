import json


def data_to_json():
    '''
    :return: Открываем файл JSON
    '''
    with open('file.json') as file:
        data = json.load(file)
        return data


def filter_data(data):
    '''

    :param data: Данные из Json
    :return:
    '''
    filters = [key for key in data if 'state' in key and key['state'] == 'EXECUTED']
    return filters


# filter_data(data)
# print(data_to_json())
