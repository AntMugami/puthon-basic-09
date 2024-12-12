main_menu = [
    'Телефонный справочник',
    'открыть существующий справочник',
    'соранить изменения в базу',
    'показать все контакты',
    'создать контакт',
    'найти контакт',
    'изменить контакт',
    'удалить контакт',
    'выход'
]


main_menu_choice = 'Выберите пункт меню: '


exit_and_buy = 'Программа закрыта!'

empty_phonebook_error = 'Телефонная книга не загружена или пуста.'

open_successful = 'Телефонная книга открыта'

save_successful = 'Телефонная книга сохранена'

new_contact_message = 'Добавление нового контакта'
new_contact_prompts = [
    'Введите имя: ',
    'Введите номер телефона: ',
    'Введите комментарий: '
]

contact_added_succsesfuly = 'Контакт успешно добавлен!'

contacts_not_found = 'Контакты не найдены!'

finded_contact = 'Найдены следующие контакты: '


input_seach_string = 'Ведите строку для поиска: '

input_id_to_change = 'Введите ID контакта для изменения: '

input_id_to_delete = 'Введите ID контакта для удаления: '

err_id = 'Нет такого ID! Повторите попутку с правильным ID контата!'


def main_menu_err_item(len_menu: int) -> str:
    return f'Введите целое число от 1 до {len_menu}'


def change_contact(id_to_change: str, contact: list[str]):
    return f"Контакт с  ID {id_to_change} изменен на:\n 'Имя: '{contact[0]} 'Телефон: '{contact[1]} 'Комментарий: '{contact[2]}"


def delete_contact(id_to_delete: str):
    return f"Контакт с  ID {id_to_delete} удален"
