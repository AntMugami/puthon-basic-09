import csv
from pathlib import Path
import os
from string import ascii_lowercase
import re


db_file = Path('./homework_01/data/database.csv') # Путь к БД


def open_db():
    '''Функция открытия телефонного справочника'''
    phonebook = []
    with open(db_file, 'r', encoding='UTF-8') as data_file:
        csv_reader = csv.reader(data_file, delimiter=';')
        for row in csv_reader:
            phonebook.append(row)
    return phonebook


def save_db(phonebook: list):
    '''Функция сохранения телефонного справочника'''
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
 

def list_contacts(phone_list: list):
    '''Отобразить текущий телефонный справочник'''
    for item in phone_list:
        id, name, phone, details = item
        print(f'№{id} Имя: {name} Телефон: {phone} Описание: {details} ')


def new_contact(phone_list: list):
    '''Добавить новый контакт'''
    new_cont_list = []
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    detail = input('Введите описание: ')
    new_cont_list = [len(phone_list), name, phone, detail]
    phone_list.append(new_cont_list)
    print('Новый контакт добавлен')
    return phone_list


def find_contact(phone_list: list):
    '''Найти контакт по имени или телефону'''
    matched_contacts = []
    search_string = input('Что будем искать? Введите данные: ')
    for items in phone_list:
        id, name, phone, detailes = items
        if re.search(search_string.lower(), name.lower()):
            match_item = [id, name, phone, detailes]
            matched_contacts.append(match_item)
        if re.search(search_string.lower(), phone.lower()):
            match_item = [id, name, phone, detailes]
            matched_contacts.append(match_item)
    return matched_contacts


def chage_contact(phone_list: list):
    '''Изменить контакт выбрав его по ID'''
    id_for_change = input('Введите ID контакта для изменения: ')
    try:
        id_for_change = int(id_for_change)
        name = input('Введите имя: ')
        phone = input('Введите телефон: ')
        detail = input('Введите описание: ')
        print(f'Контакт ID {id_for_change} Имя: {phone_list[id_for_change][1]} изменен')
        print('Новые несенные данные:')
        print(f'Контакт ID {id_for_change} Имя: {name} Номер: {phone} Описание: {detail}')
        phone_list[id_for_change] = [id_for_change, name, phone, detail]
    except:
        print('Введен неправильный ID.')
    return phone_list    


def delete_contact(phone_list: list):
    '''Удалить контакт'''
    id_for_delete = input('Введите ID контакта для удаления: ')
    try:
        id_for_delete = int(id_for_delete)
        deleted_item = phone_list.pop(id_for_delete)
        print(f'Контакт ID {deleted_item[0]} Имя: {deleted_item[1]} удален')
    except:
        print('Введен неправильный ID.')
    return phone_list


menu_content = []
for i in range(8):
    menu_content.append(str(i))


def input_menu_item():
    '''Ввод пункта меню'''
    while True:
        menu = input('>>>')
        if menu not in menu_content:
            print('Введено не число.\nВыберите нужный пункт или нажмите 0 для выхода\n')
            continue
        else:
            menu_item = int(menu)
            print('Выбран пункт', menu_item)
            return menu_item


#
# Вывод меню
#


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
    elif menu_item == 5:
            contacts_match = find_contact(phonebook)
            if contacts_match == []:
                print('Контакты не найдены!')
                continue
            else:
                print(f'Найдены следующие контакты:\n')
                for items in contacts_match:
                    id, name, phone, detailes = items
                    print(f'ID {id} Имя: {name} Телефон: {phone} Описание: {detailes}') 
                continue
    elif menu_item == 6:
            phonebook = chage_contact(phonebook)
            continue
    elif menu_item == 7:
            phonebook = delete_contact(phonebook)
            continue
    else:
            print('Выбранного пункта не существует! Повторите ввод, используйте цифры от 0 до 7')

