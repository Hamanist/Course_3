import json
from datetime import datetime


def data_to_json():
    """
    :return: Открываем файл JSON
    """
    with open('file.json') as file:
        data = json.load(file)
        return data


def filter_data(data, filter_from=False):
    """
    :param data: Данные из Json и Фильтруем JSON по ключу 'state' со значением 'executed' и его поиска в словаре.
    :param filter_from: Фильтруем JSON по ключу 'from' для его поиска в словаре.
    :return: Возвращает нужные ключи и значение.
    """
    filters = [key for key in data if 'state' in key and key['state'] == 'EXECUTED']
    if filter_from:
        filters = [key for key in data if 'from' in key]

    return filters


def last_executed(data, latest_values):
    """
    :param data: Данные из Json
    :param latest_values: Переменная с кол-вом нужных нам для возврата словарей.
    :return: Возвращает из Json сортированный список по ключу 'date'
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:latest_values]


def data_formatting(data):
    """
    :param data: Данные из Json
    :return: Возвращает дату в нужном нам формате,
    выводит перевод организации,
    выводит данные карты и счёта в замаскированном ввиде,
    и выводим сумму в нужной валюте.
    """
    formatting = []
    for formattings in data:
        date = datetime.strptime(formattings['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        description = formattings['description']

        if 'from' in formattings:
            sender = formattings['from'].split()
            sender_bill = sender.pop(-1)
            sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** ****{sender_bill[-4:]}'
            sender_info = ' '.join(sender)
        else:
            sender_bill, sender_info = '', '[СКРЫТО]'

        recipient = f"Счет **{formattings['to'][-4:]}"
        loot = f"{formattings['operationAmount']['amount']} {formattings['operationAmount']['currency']['name']}"
        formatting.append(f'''\
{date} {description}
{sender_info} {sender_bill} -> {recipient}
{loot}
''')

    return formatting
