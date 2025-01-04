import view
import model
import prompts_ru

PATH = './homework_03/phonebook.csv'


def _user_input():
    '''Выбор пункта меню'''
    user_data = None
    while user_data != '0':
        user_data, len_menu = view.user_menu_choice()
        if model.check_user_input(user_data, len_menu):
            return user_data
        view.print_message(prompts_ru.main_menu_err_item(int(len_menu) - 1))


view.programm_exit()


def start():
    '''Проверка пунктов меню'''
    user_choice = None
    phonebook = model.PhoneBook(PATH)
    while user_choice != '0':
        view.print_main_menu()
        user_choice = _user_input()
        if user_choice == '1':
            phonebook.open()
            view.print_message(prompts_ru.open_successful)
        if user_choice == '2':
            phonebook.save()
            view.print_message(prompts_ru.save_successful)
        if user_choice == '3':
            view.show_contact_list(
                phonebook.show_contacts(), prompts_ru.empty_phonebook_error)
        if user_choice == '4':
            contact = view.user_input_contact(
                prompts_ru.new_contact_message, prompts_ru.new_contact_prompts)
            phonebook.add_new_contact(contact)
            view.print_message(prompts_ru.contact_added_succsesfuly)
        if user_choice == '5':
            search_string = view.user_input(prompts_ru.input_seach_string)
            matched_contacts = phonebook.find_contact(search_string)
            view.search_rez(matched_contacts)

        if user_choice == '6':
            id_to_change = view.user_input(prompts_ru.input_id_to_change)
            check_id = phonebook.id_in_list(id_to_change)

            if check_id:
                contact = view.user_input_contact(
                    prompts_ru.new_contact_message, prompts_ru.new_contact_prompts)
                phonebook.change_contact(id_to_change, contact)
                view.print_message(
                    prompts_ru.change_contact(id_to_change, contact))
            else:
                view.print_message(prompts_ru.err_id)
        if user_choice == '7':
            id_to_delete = view.user_input(prompts_ru.input_id_to_change)
            check_id = phonebook.id_in_list(id_to_delete)

            if check_id:
                phonebook.delete_contact(id_to_delete)
                view.print_message(
                    prompts_ru.delete_contact(id_to_delete))
            else:
                view.print_message(prompts_ru.err_id)
        if user_choice == '8':
            view.programm_exit()
            break
    if user_choice == '0':
        view.programm_exit()
