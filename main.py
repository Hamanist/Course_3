from function import data_to_json, filter_data, last_executed, data_formatting

LATEST_VALUES = 5
FILTER_FROM = True


def main():
    data = data_to_json()
    data = filter_data(data, FILTER_FROM)
    data = last_executed(data, LATEST_VALUES)
    data = data_formatting(data)
    for result in data:
        print(result)


if __name__ == '__main__':
    main()
