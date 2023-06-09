from utills.utills import load_loaded_files, filter_data, sort_data, format_data


def test_load_loaded_file():
    data = load_loaded_files()
    assert type(data) is list


def test_filter_data(item_from_conf):
    assert filter_data(item_from_conf) == [{
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    }]


def test_sort_data(sort_from_conf):
    assert sort_data(sort_from_conf) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                          'operationAmount': {'amount': '41096.24',
                                                              'currency': {'name': 'USD', 'code': 'USD'}},
                                          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
                                         {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                                          'operationAmount': {'amount': '48150.39',
                                                              'currency': {'name': 'USD', 'code': 'USD'}},
                                          'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                                          'to': 'Счет 35158586384610753655'},
                                         {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
                                          'operationAmount': {'amount': '30153.72',
                                                              'currency': {'name': 'руб.', 'code': 'RUB'}},
                                          'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                                          'to': 'Счет 43241152692663622869'},
                                         {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
                                          'operationAmount': {'amount': '62814.53',
                                                              'currency': {'name': 'руб.', 'code': 'RUB'}},
                                          'description': 'Перевод со счета на счет',
                                          'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'},
                                         {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
                                          'operationAmount': {'amount': '21344.35',
                                                              'currency': {'name': 'руб.', 'code': 'RUB'}},
                                          'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]


def test_format_dat(format_data_from_conf):
    assert format_data(format_data_from_conf) == [

        '  \n'
        '03.07.19 Перевод организации \n'
        'MasterCard 7158 30** **** 6758 --> Счет ** 5560\n'
        '8221.37 USD\n'
        '                    ',
        '  \n'
        '30.06.18 Перевод организации \n'
        'Счет 7510 68** **** 6952 --> Счет ** 6702\n'
        '9824.07 USD\n'
        '                    ',
        '\n'
        '23.03.18 Открытие вклада \n'
        'Новый счёт:  Счет ** 2431\n'
        '48223.05 руб.\n'
        '        '
    ]
