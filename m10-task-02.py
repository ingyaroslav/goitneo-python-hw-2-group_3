class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Invalid phone number. Phone number must be a 10-digit number.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        phone_numbers = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phone_numbers}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        name = str(record.name)
        self.data[name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]