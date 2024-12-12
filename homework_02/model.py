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

    def id_in_list(self, entered_id):
        if len(self.contacts) < int(entered_id):
            return False
        return True

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as data_file:
            for row in data_file.readlines():
                cont_id = self._next_id()
                name, phone, comment = row.strip().split(SEP)
                contact = Contact(cont_id, name, phone, comment)
                self.contacts.append(contact)

    def save(self):
        with open(self._path, 'w', encoding='UTF-8') as data_file:
            csv_writer = csv.writer(
                data_file, delimiter=';', lineterminator='\n')
            for row in self.contacts:
                csv_writer.writerow(row[1:])

    def add_new_contact(self, contact: list[str]) -> None:
        new_id = self._next_id()
        new_contact = Contact(new_id, *contact)
        self.contacts.append(new_contact)

    def find_contact(self, search_str: str) -> list[str]:
        matched_contacts = []
        for row in self.contacts:
            for item in row:
                if search_str.lower() in str(item).lower():
                    matched_contacts.append(row[1:])
        return matched_contacts

    def change_contact(self, id_to_change: str, new_contact: list[str]) -> bool:
        for row in self.contacts:
            if row[0] == int(id_to_change):
                self.contacts = self.contacts[:row.id -
                                              1] + self.contacts[row.id:]
                new_contact = Contact(self._next_id(), *new_contact)
                self.contacts.append(new_contact)

    def delete_contact(self, id_to_delete: str) -> None:
        for row in self.contacts:
            if row[0] == int(id_to_delete):
                self.contacts = self.contacts[:row.id -
                                              1] + self.contacts[row.id:]
        return None

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
