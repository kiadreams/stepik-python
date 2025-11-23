from collections import UserDict


# Напишите определение класса ContactBook
class ContactBook(UserDict):

    def add_contact(self, name: str, phone_number: str) -> None:
        if name in self:
            print(f'Контакт {name} уже существует')
        else:
            self[name] = phone_number
            print(f'Контакт {name} создан')

    def update_contact(self, name: str, new_phone_number: str) -> None:
        if name in self:
            self[name] = new_phone_number
        else:
            print(f'Контакт {name} не найден')

    def delete_contact(self, name: str) -> None:
        if name in self:
            del self[name]
            print(f'Контакт {name} успешно удален')
        else:
            print(f"Контакт {name} не найден")

    def display_contacts(self) -> None:
        if self:
            for name, number in self.items():
                print(f'{name}: {number}')
        else:
            print(f'Телефонный список пуст')


contact_book = ContactBook()
contact_book.add_contact("John", "123-456-7890")
assert contact_book.data['John'] == "123-456-7890"
contact_book.add_contact("John", "345-666")  # Печатает Контакт John уже существует.
contact_book.add_contact("Alice", "987-654-3210")
assert contact_book.data['Alice'] == "987-654-3210"
contact_book.display_contacts()
print('-' * 20)

contact_book.update_contact("John", "111-222-3333")
assert contact_book.data['John'] == "111-222-3333"
contact_book.display_contacts()
print('-' * 20)

contact_book.delete_contact("Alice")
assert 'Alice' not in contact_book.data
contact_book.display_contacts()
