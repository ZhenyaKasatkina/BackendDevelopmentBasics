import os.path
from config import ROOT_DIR

import pytest

from src import utils


@pytest.fixture
def coll():  # имя фикстуры любое
    file_two = [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
    }
    ]
    return file_two


def test_get_data_from_file():
    used_file = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert utils.get_data_from_file(used_file) == [1, 2, 3]


def test_get_filtered_transactions(coll):
    assert utils.get_filtered_transactions(coll) == [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }]


def test_get_sorted_transactions():
    data = [
      {
        "id": 441945886,
        "date": "2018-08-26T10:50:58.294041"
        },
      {
        "id": 41428829,
        "date": "2020-07-03T18:35:29.512364",
        },
      {
        "id": 939719570,
        "date": "2019-06-30T02:08:58.425572"
        }]
    expeted = [
      {
        "id": 41428829,
        "date": "2020-07-03T18:35:29.512364",
        },
      {
        "id": 939719570,
        "date": "2019-06-30T02:08:58.425572"
        },
      {
            "id": 441945886,
            "date": "2018-08-26T10:50:58.294041"
        }]
    assert utils.get_sorted_transactions(data) == expeted


def test_hide_bank_account():
    assert utils.hide_bank_account('Счет 71687416928274675290') == 'Счет  **5290'
    assert utils.hide_bank_account("Visa Classic 2842873333339012") == "Visa Classic  2842 87** **** 9012"
    assert utils.hide_bank_account(None) == " None **** **"


def test_change_format_date():
    assert utils.change_format_date("2019-07-18T12:27:13.355343") == "18.07.2019"


def test_get_display_of_amount_and_currency():
    file_four = {"key_test": {"amount": "82139.20", "currency": {"name": "руб.", "code": "RUB"}}}
    assert utils.get_display_of_amount_and_currency(file_four['key_test']) == "82139.20 руб."


def test_print_the_result(coll):
    file_three = ("\n13.07.2019 Перевод с карты на счет\
\nMaestro  1308 79** **** 7170 -> Счет  **8612\
\n97853.86 руб.\n\
\n14.10.2018 Перевод с карты на счет\
\nMaestro  3928 54** **** 4026 -> Счет  **3493\
\n77751.04 руб.")
    assert utils.print_the_result(coll) == file_three
