import csv
from pathlib import Path
import os
from string import ascii_lowercase
#
db_file = Path('./homework_01/data/database.csv')

#Открытие и сохранение
#
def open_db():
    phonebook = []

    # print(os.path.isfile(db_file))
    with open(db_file, 'r', encoding='UTF-8') as data_file:
        csv_reader = csv.reader(data_file, delimiter=';')
        for row in csv_reader:
            # print(row)
            phonebook.append(row)
    # print(phonebook)
    return phonebook

def save_db(phonebook):
    if phonebook == []:
        print('''
               Адресная книга не загружена или пуста!!!
               Все дынные будут удалены!!!
               Вы хотите подолжить?
               ''')
        answer = input('Введите Y- для продолжения и любой другой символ для отмены: ')
        if answer.lower == 'y':
            print('Данные стираюся!!!')
            with open(db_file, 'w', encoding='UTF-8') as data_file:
                csv_writer = csv.writer(data_file, delimiter=';',lineterminator='\n')
                csv_writer.writerows(phonebook)
    print('Адресная книга сохранена!')
    with open(db_file, 'w', encoding='UTF-8') as data_file:
                csv_writer = csv.writer(data_file, delimiter=';',lineterminator='\n')
                csv_writer.writerows(phonebook) 


#
#Навинация
#

def list_contacts(phone_list):
    for item in phone_list:
        id, name, phone, details = item
        print(f'№{id} Имя: {name} Телефон: {phone} Описание: {details} ')

def new_contact(phone_list):
    new_cont_list = []
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    detail = input('Введите описание: ')
    new_cont_list = [len(phone_list), name, phone, detail]
    phone_list.append(new_cont_list)
    # print(phone_list)
    # print(new_cont_list)
    print('Новый контакт добавлен')
    # print(phone_list_udated)
    return phone_list

def find_contact(phone_list):
    pass

def chage_contact(phone_list):
    pass

def delete_contact(phone_list):
    pass

menu_content = []
for i in range(8):
    menu_content.append(str(i))



def input_menu_item(): # Ввод пункта меню
    while True:
        menu = input('>>>')
        if menu not in menu_content:
            print('Введено не число.\nВыберите нужный пункт или нажмите 0 для выхода\n')
            continue
        else:
            menu_item = int(menu)
            print('Выбран пункт', menu_item)
            return menu_item
    # return menu_item
#
# Анализ навигвции по введенным пунктам
#  
def analys_choisen_item(menu_item, phonebook):
    phone_list = phonebook
    # if menu_item == 3:
    #     print(phone_list)
    #     if phone_list == []:
    #         print('Справочник пуст! Закрузине справочник или внесите контакты.')
    #         # menu_item = input_menu_item()
    #     else:
    #         list_contacts(phone_list)
        # print('Выберите новый пункт меню:\n')
        # menu_item = input_menu_item()
    # elif menu_item == 4:
    #     updated_phone_list = new_contact(phone_list)
    #     return updated_phone_list
        # print('Выберите новый пункт меню:\n')
        # menu_item = input_menu_item()
    if menu_item == 5:
        find_contact(phone_list)
        # print('Выберите новый пункт меню:\n')
        # menu_item = input_menu_item()
    if menu_item == 6:
        chage_contact(phone_list)
        # print('Выберите новый пункт меню:\n')
        # menu_item = input_menu_item()
    if menu_item == 7:
        delete_contact(phone_list)
        # print('Выберите новый пункт меню:\n')
        # menu_item = input_menu_item()
    # elif menu_item == 0:
    #     print('Работа завершена! Пока!\n')

#
# Вывод меню
#
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
# menu_item = input_menu_item()

while True:
    menu_item = input_menu_item()
    if menu_item == 0:
        print('Работа завершена! Пока!\n')
        break

    elif menu_item == 1:
            # print('Начало загрузки')
            phonebook = open_db()
            # print(phonebook)
    elif menu_item == 2:
            save_db(phonebook)
    elif menu_item == 3:
            if phonebook == []:
                print('Справочник пуст! Закрузине справочник или внесите контакты.')
            # menu_item = input_menu_item()
            else:
                list_contacts(phonebook)
    elif menu_item == 4:
            phonebook = new_contact(phonebook)
            continue
    else:
            analys_choisen_item(menu_item, phonebook)



# print(open_db())
# print(open_db()[0][0])
# print(open_db()[0][1])
# print(open_db()[2][3])
# print(open_db()[1][2])
# print(open_db()[3][3])