from func_json import data_to_json


def main():
    data = data_to_json()
    return len(data['id'])



if __name__ == '__main__':
    main()
