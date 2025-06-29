def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter the name and phone number after the 'add' or 'change' command."
        except IndexError:
            return "Please enter the name after the 'phone' command."
        except KeyError:
            return "Please enter a valid name from your contact list"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
def show_phone_number(args, contacts):
    return f"{args[0]} phone number: {contacts[args[0]]}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone_number(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()