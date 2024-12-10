import view
import model
import prompts_ru

PATH = './homework_02/phonebook.csv'


def _user_input():
    while True:
        user_data, len_menu = view.user_menu_choice()
        if model.check_user_input(user_data, len_menu):
            return user_data
        view.print_message(prompts_ru.main_menu_err_item(int(len_menu) - 1))


def start():
    phonebook = model.PhoneBook(PATH)
    while True:
        view.print_main_menu()
        user_choice = _user_input()
        if user_choice == '1':
            phonebook.open()
        if user_choice == '2':
            print('Сохранить файл')
        if user_choice == '3':
            view.show_contact_list(
                phonebook.show_contacts(), prompts_ru.empty_phonebook_error)
        if user_choice == '4':
            print('Создать контакт')
        if user_choice == '5':
            print('Найти контакт')
        if user_choice == '6':
            print('Изменить контакт')
        if user_choice == '7':
            print('Удалить контакт')
        if user_choice == '8':
            view.programm_exit()
            break
