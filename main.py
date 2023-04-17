from utills.apelsin import load_loaded_files, filter_data, sort_data, space_data

def main():
    data = load_loaded_files() # get data from files
    print(data)
    dat = filter_data(data)# Исключение значений, у которых стоит не EXECUTED
    print(dat)
    print(sort_data(data))
    print(space_data(data))

if __name__ == '__main__':
    main()