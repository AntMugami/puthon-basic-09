import pytest
import model
from controller import PATH
from unittest import mock


@pytest.mark.parametrize(
    "name, phone, comment",
    [
        ('Антон', 9161234567, 'Тест комментария 1'),
         ('Федот', 9161236767, 'Тест комментария 2'),
    ]
)


def test_add_new_contact(name, phone, comment):
    '''Тест добавления контакта'''
    pb = model.PhoneBook(PATH)
    contact = [name, phone, comment]
    cont_list  = [1]
    assert pb.add_new_contact(contact) == cont_list.append(contact)


@pytest.fixture
def contact_to_test():
    return [
        'Антон', 9161234567, 'Тест комментария 1'
    ]


@pytest.fixture
def contact_change():
    return [
        'Федот', 9161236767, 'Тест комментария 2'
    ]


def test_find_contact_found_name(contact_to_test):
    '''Тест поиска контакта по имени'''
    name, phone, comment = contact_to_test
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    assert pb.find_contact(name) == [tuple(contact_to_test)]


def test_find_contact_found_phone(contact_to_test):
    '''Тест поиска контакта по телефону'''
    name, phone, comment = contact_to_test
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    assert pb.find_contact(str(phone)) == [tuple(contact_to_test)]


def test_find_contact_not_found(contact_to_test):
    '''Тест поиска контакта, который отсутствует в Телефонной книге'''
    name, phone, comment = contact_to_test
    name += '1'
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    assert pb.find_contact(name) == []


def test_change_contact(contact_to_test, contact_change):
    '''Тест изменения контакта'''
    name, phone, comment = contact_change
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    pb.change_contact('1', contact_change)
    assert  pb.find_contact(name) == [tuple(contact_change)]


def test_delete_contact(contact_to_test):
    '''Тест удаления контакта'''
    name, phone, comment = contact_to_test
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    pb.delete_contact('1')
    assert  pb.find_contact(name) == []

def test_delete_contact_wrong_id(contact_to_test):
    '''Тест удаления контакта'''
    name, phone, comment = contact_to_test
    pb = model.PhoneBook(PATH)
    pb.add_new_contact(contact_to_test)
    pb.delete_contact('2')
    assert  pb.find_contact(name) != []


def test_open():
    '''Тест чтения из файла адресной книги'''
    fake_path = './test_phonebook.csv'
    pb = model.PhoneBook(fake_path)
    pb.open()
    print(pb.show_contacts())
    assert pb.show_contacts() != {}

def test_save(contact_change):
    '''Тест записи файла адресной книги'''
    fake_path_2 = './test_save_phonebook.csv'
    name, phone, comment = contact_change
    pb = model.PhoneBook(fake_path_2)
    pb.add_new_contact(contact_change)
    with mock.patch('builtins.open', mock.mock_open()) as open_:
        pb.save()
        assert open_().write.call_args_list == [mock.call(f'{name};{phone};{comment}\n')]


