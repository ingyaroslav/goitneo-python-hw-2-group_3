class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                name, phone = args
                record = Record(name)
                record.add_phone(phone)
                contacts[name] = record
                print("Contact added.")
            elif command == "change":
                name, phone = args
                if name in contacts:
                    contacts[name].edit_phone(contacts[name].phones[0].value, phone)
                    print("Contact updated.")
                else:
                    print(f"Contact with name '{name}' not found.")
            elif command == "phone":
                name = args[0]
                if name in contacts:
                    print(contacts[name].phones[0].value)
                else:
                    print(f"Contact with name '{name}' not found.")
            elif command == "all":
                if contacts:
                    for name, record in contacts.items():
                        print(f"{name}: {record.phones[0].value}")
                else:
                    print("No contacts available.")
            else:
                print("Invalid command.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
