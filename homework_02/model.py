import csv
from collections import namedtuple


def check_user_input(user_data: str, len_menu: int) -> bool:
    if user_data.isdigit() and (0 < int(user_data) < len_menu):
        return True
    return False


SEP = ';'

Contact = namedtuple('Contact', 'id name phone comment')


class PhoneBook:
    def __init__(self, path):
        self._path = path
        self.contacts: list[Contact] = []

    def _next_id(self):
        if not self.contacts:
            return 1
        return self.contacts[-1].id + 1

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as data_file:
            # csv_reader = csv.reader(data_file, delimiter=';')
            for row in data_file.readlines():
                # name, phone, comment = row.strip().split(SEP)
                cont_id = self._next_id()
                name, phone, comment = row.strip().split(SEP)
                contact = Contact(cont_id, name, phone, comment)
                self.contacts.append(contact)

    @staticmethod
    def _convert_to_json(contacts_list: list[Contact]):
        _json = {}
        for contact in contacts_list:
            _json[contact.id] = {
                'name': contact.name,
                'phone': contact.phone,
                'comment': contact.comment,
            }
        return _json

    def show_contacts(self):
        return self._convert_to_json(self.contacts)
