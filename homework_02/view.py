import prompts_ru


def print_main_menu():
    '''Отображение главного меню'''
    menu_items = prompts_ru.main_menu
    for no, text in enumerate(menu_items):
        if no:
            print(f'\t{no} - {text}')
        else:
            print(f'{text}')


def user_input(message: str) -> str:
    '''Поучение данных от пользователя'''
    return input(message).strip()


def user_menu_choice():
    return user_input(prompts_ru.main_menu_choice), len(prompts_ru.main_menu)


def user_input_contact(input_message: str, contact_fields: list[str]) -> list[str]:
    print(input_message)
    new_contact = []
    for item in contact_fields:
        row = user_input(item)
        new_contact.append(row)
    return new_contact


def programm_exit():
    print(prompts_ru.exit_and_buy)
    return None


def print_message(message: str) -> None:
    print('\n')
    print('='*len(message))
    print(message)
    print('='*len(message) + '\n')


def show_contact_list(contact_list: dict[str, str], mess_error: str) -> None:
    if contact_list:
        for cont_id, item in contact_list.items():
            print(f"{cont_id} - {item['name']
                                 } {item['phone']} {item['comment']}")
    else:
        print_message(mess_error)


def search_rez(matched_contacts: list[str]):
    if matched_contacts:
        for row in matched_contacts:
            print(f"'Имя: '{row[0]} 'Телефон: '{
                  row[1]}")

    else:
        print_message(prompts_ru.contacts_not_found)
