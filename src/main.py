import os
from config import ROOT_DIR
from src.utils import get_data_from_file, get_filtered_transactions, get_sorted_transactions, print_the_result


# файл с данными операций клиента Банка
used_file = os.path.join(ROOT_DIR, 'src', 'operations.json')


def main(file):
    all_data_from_file = get_data_from_file(file)
    filtered_transactions = get_filtered_transactions(all_data_from_file)
    sorted_file_by_date = get_sorted_transactions(filtered_transactions)
    last_five_operations = sorted_file_by_date[:5]   # выбовод последних 5 операций
    data_operation = print_the_result(last_five_operations)
    print(data_operation)


if __name__ == "__main__":
    main(used_file)
