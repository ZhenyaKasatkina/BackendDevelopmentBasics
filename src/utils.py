import json

def get_data_from_file(path):
    """Получение выполненных операций клиента Банка из файла"""
    with open(path) as file:
        data_file = json.load(file)
        return data_file
