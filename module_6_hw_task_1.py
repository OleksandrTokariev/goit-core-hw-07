from collections import UserDict

class UncorrectPhone(ValueError):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if (len(phone) == 10) and (phone.isdigit()):
            super().__init__(phone)
        else:
            raise UncorrectPhone(f"Phone number contain more or less than 10 digits only")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
        else:
            raise ValueError(f"Номер телефону '{old_phone}' не знайдено")

    def find_phone(self, search_phone: str) -> Phone | None:
        for phone_obj in self.phones:
            if search_phone == phone_obj.value:
                return phone_obj
        return None

    def remove_phone(self, deleted_phone: str):
        phone_obj = self.find_phone(deleted_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError(f"Номер телефону '{deleted_phone}' не знайдено")
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, new_record: Record):
        self.data[new_record.name.value] = new_record  # ключ - ім"я (Record)

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)  # вернуть Record или None

    def delete(self, deleted_name: str):
        self.data.pop(deleted_name)

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення конкретного телефону у записі John
john.remove_phone("5555555555")
print(john, "\n-----------------------")
print(book, "\n-----------------------")

# Видалення запису Jane
book.delete("Jane")
print(book)