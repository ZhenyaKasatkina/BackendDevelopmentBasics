import json


def get_data_from_file(path):
    """Получение выполненных операций клиента Банка из файла"""
    with open(path) as file:
        data_file = json.load(file)
        return data_file


def get_filtered_transactions(data_file):
    file_executed_state = []
    for transaction in data_file:
        if transaction.get('state') == "EXECUTED":
            file_executed_state.append(transaction)
    return file_executed_state
