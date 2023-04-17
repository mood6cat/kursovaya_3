import json


def load_files():
    with open("operations.json", 'r', encoding="utf-8") as f:
        files = json.load(f)
    return files

def load_loaded_files():
    return load_files()

def filter_data(data):
    """Вернуть значение только с EXECUTED"""
    filtered = [x for x in data if "state" in x and x["state"] == "EXECUTED"]  #Списковое включение
    return filtered

def sort_data(data):
    """Сортируем 5 первых значений через ЛЯМБДА-ФУНКЦИЮ"""
    xx = lambda x: x['date']
    data = sorted(data, key=xx, reverse=True)
    # t=[x['date'] for x in data]
    # for v in t:
    #     print(v)
    return data[:5]

def space_data(data):
    pass
