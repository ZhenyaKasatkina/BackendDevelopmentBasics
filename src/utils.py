import json
import datetime


def get_data_from_file(path):
    """Получение выполненных операций клиента Банка из файла"""
    with open(path) as file:
        data_file = json.load(file)
        return data_file


def get_filtered_transactions(data_file):
    """Фильтрация операций по статусу 'Выполнено'"""
    file_executed_state = []
    for transaction in data_file:
        if transaction.get('state') == "EXECUTED":
            file_executed_state.append(transaction)
    return file_executed_state


def get_sorted_transactions(file_executed_state):
    """Сортировка операций по дате убывания"""
    sorted_data_file = sorted(file_executed_state, key=lambda x: x['date'], reverse=True)
    last_five_operations = sorted_data_file[:5]
    return last_five_operations


def change_format_date(the_date):
    """Изменение формата даты"""
    format_date = datetime.datetime.strptime(the_date, '%Y-%m-%dT%H:%M:%S.%f')
    return format_date.strftime('%d.%m.%Y')


def hide_bank_account(card_account):
    """Скрывает данные банковского счета/карты"""
    account_client = str(card_account)
    if "Счет" in account_client:
        type_account = (list(str(account_client)))[:-20]
        account = (list(str(account_client)))[-20:]
        number_account = account[-4:]
        return f'{"".join(type_account)} {"**"}{"".join(number_account)}'
    else:
        type_account = (list(str(account_client)))[:-16]
        account = (list(str(account_client)))[-16:]
        account[6:12] = '******'
        chunk_size = 4
        new_account = [account[i:i + chunk_size] for i in range(0, len(account), chunk_size)]
        number_account = []
        for i in new_account:
            number_account += "".join(i) + " "
        return f'{"".join(type_account)} {"".join(number_account).rstrip()}'


def get_display_of_amount_and_currency(size_of_operation):
    """Получает отображение суммы операции и денежной единицы"""
    return f"{size_of_operation['amount']} {size_of_operation['currency']['name']}"


def print_the_result(data_from_file):
    """Выводит операции в необходимом формате"""
    list_result = []
    for item in data_from_file:
        result = f"\n{change_format_date(item.get('date'))} {item.get('description')}" \
               f"\n{hide_bank_account(item.get('from'))} {'->'} {hide_bank_account(item.get('to'))}"\
               f"\n{get_display_of_amount_and_currency(item.get('operationAmount'))}"
        list_result.append(result)
    return "\n".join(list_result)
