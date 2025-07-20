from collections import UserDict
from datetime import datetime, date, timedelta

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

class Birthday(Field):
    def __init__(self, value):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(parsed_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)

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
        self.data[new_record.name.value] = new_record

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def delete(self, deleted_name: str):
        self.data.pop(deleted_name)

    @staticmethod
    def __date_to_string(date):
        return date.strftime("%Y.%m.%d")

    @staticmethod
    def __find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    @staticmethod
    def __adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            return AddressBook.__find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if 0 <= (birthday_this_year - today).days <= days:
                    birthday_this_year = AddressBook.__adjust_for_weekend(birthday_this_year)
                    congratulation_date_str = AddressBook.__date_to_string(birthday_this_year)
                    upcoming_birthdays.append({"name": record.name.value,
                                               "birthday": AddressBook.__date_to_string(record.birthday.value),
                                               "congratulation_date": congratulation_date_str})
        return upcoming_birthdays

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UncorrectPhone as e:
            return str(e)
        except ValueError:
            return "Please enter the name and phone number after the 'add' or 'change' command."
        except IndexError:
            return "Please enter the name after the 'phone' command."
        except KeyError:
            return "Please enter a valid name from your contact list"
    return inner

@input_error
def add_contact(args, address_book: AddressBook):
    name, phone, *_ = args
    record = address_book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        address_book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, address_book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = address_book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
    return "Contact changed."

@input_error
def show_phone_number(args, address_book: AddressBook):
    name, *_ = args
    record = address_book.find(name)
    if record:
        return record

@input_error
def add_birthday(args, address_book: AddressBook):
    name, birth_date, *_ = args
    record = address_book.find(name)
    if record:
        record.add_birthday(birth_date)
    return "Birthday added."

@input_error
def show_birthday(args, address_book: AddressBook):
    name, *_ = args
    record = address_book.find(name)
    if record:
        return record.birthday

@input_error
def birthdays(address_book: AddressBook):
    birthdays_list = address_book.get_upcoming_birthdays()
    if birthdays_list:
        return birthdays_list
    else:
        return "There are no birthdays in the next 7 days"

def main():
    test_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, test_book))
        elif command == "all":
            print(test_book)
        elif command == "change":
            print(change_contact(args, test_book))
        elif command == "phone":
            print(show_phone_number(args, test_book))
        elif command == "add-birthday":
            print(add_birthday(args, test_book))
        elif command == "show-birthday":
            print(show_birthday(args, test_book))
        elif command == "birthdays":
            print(birthdays(test_book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()