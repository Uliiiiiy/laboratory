import csv
with open('FIOandTelephone.csv', "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, ["FIO", 'Telephone'])
    fio = input('Введите ФИО человека: ')
    for i in reader:
        i = dict(i)
        if fio == i['FIO']:
            print('Номер телефона: ', i['Telephone'])
            break
    else:
        print('Нет в телефонной книге')