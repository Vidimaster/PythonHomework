from copy import deepcopy


class PhoneBook:
    def __init__(self, path: str = 'phone.txt'):
        self.path = 'phone.txt'
        self.phone_book = {}
        self.original_book = {}
        self.favorite = False

    def open_file(self):
        with open (self.path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
        for i, contact in enumerate(data):
            contact = contact.strip().split(';')
            self.phone_book[i] = contact
        self.original_book = deepcopy(self.phone_book)

    def save_file(self):
        data = []
        for contact in self.phone_book.values():
            contact = ';'.join(contact)
            data.append(contact)
        data = '\n'.join(data)
        with open (self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def add_contact(self, new_contact: list):
        c_id = max(self.phone_book) + 1
        self.phone_book[c_id] = new_contact

    def find_contact (self, word: str):
        result = {}
        for c_id, contact in self.phone_book.items():
            for field in contact:
                if word.lower() in field.lower():
                    result[c_id] = contact
                    break
        return result
        
    def edit_contact(self, c_id: int, new_contact: list):
        current_contact = self.phone_book.get(c_id)
        contact = []
        for i in range(len(new_contact)):
            if new_contact[i]:
                contact.append(new_contact[i])
            else:
                contact.append(current_contact[i])
        self.phone_book[c_id] = contact
        return contact[0]

    def delete_contact(self, c_id: int) -> str:
        return self.phone_book.pop(c_id)[0]
    
    def make_contact_favorite (self, c_id: int):
        if self.phone_book[c_id][3] == "true":
            self.phone_book[c_id][3] = "false"
        else:
            self.phone_book[c_id][3] = "true"
        return self.phone_book[c_id][0]