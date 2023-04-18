from utills.apelsin import load_loaded_files, filter_data, sort_data, format_data

def main():
    data = load_loaded_files() # get data from files
    data = filter_data(data)# Исключение значений, у которых стоит не EXECUTED
    data = sort_data(data)
    data = format_data
    for value in data:
        print(value)
if __name__ == '__main__':
    main()