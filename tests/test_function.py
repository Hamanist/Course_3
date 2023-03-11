from function import last_executed


def test_last_executed(test_data):
    data = last_executed(test_data, latest_values=3)
    assert len(data) == 3
    assert data[0]['date'] == '2022-06-30T02:08:58.425572'


