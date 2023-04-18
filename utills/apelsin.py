import json
import time
from datetime import datetime


def load_files():
    """Загрузить файл"""
    with open("operations.json", 'r', encoding="utf-8") as f:
        files = json.load(f)
    return files


def load_loaded_files():
    """Вернуть загруженный файл"""
    return load_files()


def filter_data(data):
    """Вернуть значение только с EXECUTED"""
    filtered = [x for x in data if "state" in x and x["state"] == "EXECUTED"]  # Списковое включение
    return filtered


def sort_data(data):
    """Сортируем 5 первых значений через ЛЯМБДА-ФУНКЦИЮ"""
    xx = lambda x: x['date']
    data = sorted(data, key=xx, reverse=True)
    # t=[x['date'] for x in data]
    # for v in t:
    #     print(v)
    return data[:5]


def format_data(data):
    """
    # Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
Форматирование даты и счетов
    :param data:
    :return:
    """
    formated_data = []
    for value in data:
        date = datetime.strptime(value['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%y")
        desc = value["description"]  # Может быть несколько пробелов, и мы знаем это
        from_arrow=''
        if "from" in value:
            from_arrow='-->'
            sender = value['from'].split()  # Сплитим по пробелам
            sen_b = sender.pop(-1)  # Забрать последнее значение через pop, Удаляя его
            sen_i = ' '.join(sender)  # Мы уверены, что первое наше значение - это какой-то счёт или VISA CLASSIC, Делаем join
            # Теперь нужно отформатировать по звёздочкам, как в комменте
            sen_b = f"{sen_b[:4]} {sen_b[4:6]}** **** {sen_b[-4:]}"
        else:
            sen_i = ''
            sen_b = ''
            from_arrow = "->"

        formated_data.append(f"""
        {date} {desc} 
        {sen_i} {sen_b} {from_arrow}
        """)
        return formated_data