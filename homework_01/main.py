import csv
from pathlib import Path

db_file = Path('./homework_01/data/database.csv')
# print(db_file)


def open_db():
    phonebook = []
    with open(db_file, 'r', encoding='UTF-8') as data_file:
        csv_reader = csv.reader(data_file, delimiter=';')
        for row in csv_reader:
            phonebook.append(row)
    return phonebook

def save_db():
    with open(db_file, 'w', encoding='UTF-8') as data_file:
        csv_writer = csv.writer(data_file, delimiter=';',lineterminator='\n')
        csv_writer.writerows(data_file)

def list_contacts(phonebook):
    print(phonebook)

def new_contact():
    pass

def find_contact():
    pass

def chage_contact():
    pass

def delete_contact():
    pass

menu_content = []
for i in range(8):
    menu_content.append(str(i))

def input_menu_item():
    while True:
        menu = input()
        if menu not in menu_content:
            print('Введено не число.\nВыберите нужный пункт или нажмите 0 для выхода\n')
            continue
        else:
            menu_item = int(menu)
            print('Выбран пункт', menu_item)
            break
    return menu_item
    
def analys_choisen_item(menu_item):
    if menu_item == 1:
        phonebook = open_db()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
        return phonebook
    elif menu_item == 2:
        save_db()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
    elif menu_item == 3:
            if phonebook == []:
                print('Справочник пуст! Закрузине справочник или внесите контакты.')
                menu_item = input_menu_item()
            else:
                list_contacts(phonebook)
            print('Выберите новый пункт меню:\n')
            menu_item = input_menu_item()
    elif menu_item == 4:
        new_contact()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
    elif menu_item == 5:
        find_contact()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
    elif menu_item == 6:
        chage_contact()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
    elif menu_item == 7:
        delete_contact()
        print('Выберите новый пункт меню:\n')
        menu_item = input_menu_item()
    elif menu_item == 0:
        print('Работа завершена! Пока!\n')


print(menu_content)
print('''
      Это телефонный справочник\n
      для навигации необходимо использовать цифры:\n
      1 - открыть существующий справочник
      2 - соранить изменения в базу
      3 - показать все контакты
      4 - создать контакт
      5 - найти контакт
      6 - изменить контакт
      7 - удалить контакт
      0 - выход\n
      выберите один из пунктов 
    ''')

phonebook = []
menu_item = input_menu_item()

while True:
    menu_item = input_menu_item()
    if menu_item == 0:
        print('Работа завершена! Пока!\n')
    else:
        analys_choisen_item(menu_item)



# print(open_db())
# print(open_db()[0][0])
# print(open_db()[0][1])
# print(open_db()[2][3])
# print(open_db()[1][2])
# print(open_db()[3][3])