import csv
import random

f = "db.csv"
list_dict =[] # будет список словарей
with open(f, "r", newline='', encoding ='utf-8') as f:
    r = csv.DictReader(f, delimiter=',')
    for row in r:
        row['оклад'] = str(random.randint(20, 60)*800) # изменяем оклад на слуйчайное значение random
        d = dict(row.items()) # создаем словарь из строки
        list_dict.append(d) # добавляем словарь в список
        print(row['ID'], row['фамилия'], row['имя'], row['отчество'],' оклад =', row['оклад'])

# делаем копии       
with open('db_copy.csv', 'w', newline='', encoding ='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(list_dict[0].keys()))
    writer.writeheader()
    for i in list_dict:
        writer.writerow(i)
        
# делаем копии 
with open('../db_personnel_copy.csv', 'w', newline='', encoding ='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(list_dict[0].keys()))
    writer.writeheader()
    for i in list_dict:
        writer.writerow(i)
