def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input error: {e}")
    return wrapper


@input_error
def add_contact(phonebook, name, number):
    """
    Додає контакт у телефонну книгу.
    """
    phonebook[name] = number
    print(f"Contact '{name}' with number '{number}' added successfully.")


@input_error
def change_contact(phonebook, name, new_number):
    """
    Змінює номер телефону для вказаного контакту.
    """
    if name in phonebook:
        phonebook[name] = new_number
        print(f"Number for contact '{name}' changed to '{new_number}'.")
    else:
        raise KeyError(f"Contact '{name}' not found in the phonebook.")


@input_error
def show_phone(phonebook, name):
    """
    Виводить номер телефону для вказаного контакту.
    """
    print(f"The phone number for '{name}' is {phonebook[name]}.")


@input_error
def show_all_contacts(phonebook):
    """
    Виводить всі контакти телефонної книги.
    """
    print("All contacts in the phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")


def parse_input(command):
    """
    Розбирає введену користувачем команду.
    Повертає кортеж (команда, аргументи).
    """
    parts = command.split()
    if parts:
        return parts[0].lower(), parts[1:]
    return "", []


def main():
    print("Welcome to the assistant bot!")
    phonebook = {}
    while True:
        command = input("Enter a command: ").strip()

        if command.lower() in ["close", "exit"]:
            print("Good bye!")
            break

        cmd, args = parse_input(command)

        if cmd == "hello":
            print("How can I help you?")

        elif cmd == "add":
            if len(args) == 2:
                add_contact(phonebook, args[0], args[1])
            else:
                print("Invalid number of arguments for 'add' command.")

        elif cmd == "change":
            if len(args) == 2:
                change_contact(phonebook, args[0], args[1])
            else:
                print("Invalid number of arguments for 'change' command.")

        elif cmd == "show":
            if len(args) == 1:
                show_phone(phonebook, args[0])
            elif len(args) == 0:
                show_all_contacts(phonebook)
            else:
                print("Invalid number of arguments for 'show' command.")

        else:
            print("Invalid command. Type again!")


if __name__ == "__main__":
    main()
