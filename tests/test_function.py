from conftest import test_data
from function import last_executed, data_to_json, filter_data, data_formatting


def test_data_to_json(test_data):
    data = data_to_json()
    assert data[:1] == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                         'to': 'Счет 64686473678894779589'}]


def test_last_executed(test_data):
    data = last_executed(test_data, latest_values=3)
    assert len(data) == 3
    assert data[0]['date'] == '2022-06-30T02:08:58.425572'


def test_filter_data(test_data):
    data = filter_data(test_data)
    assert len(data) == 14
    assert len(filter_data(test_data, filter_from=True)) == 13


def test_data_formatting(test_data):
    data = data_formatting(test_data[:1])

    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** ****5199-> Счет **9589\n31957.58 руб.\n']


def test_data_formatting_no_from(test_data):
    data = data_formatting(test_data[3:4])
    assert data == ['23.03.2018 Открытие вклада\n[СКРЫТО] -> Счет **2431\n48223.05 руб.\n']
