import csv

f = True

def run():
    
    def csv_reader(fio):
        """ Чтение файла csv и поиск по фамилии
        """
        path_csv_file = "db_personnel_copy.csv"
        with open(path_csv_file, "r", newline="", encoding ='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                if fio == row['фамилия'][0:len(fio)]: # поиск и сравнение
                    print(row['ID'],row['фамилия'],row['имя'],row['отчество'],' оклад =', row['оклад'])
                    
    fio = str.upper(input('Введите первые 1 - 3 буквы Фамилии сотрудника: '))
    print('_______________\nзакрыть Alt+F4\n')
    
    csv_reader(fio)

while f:
    run()    
