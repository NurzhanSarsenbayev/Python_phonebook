class PhoneBook:
    def __init__(self, path: str = 'phone.txt'):
        self.phone_book = list[dict[str, str]] = []
        self.path = path

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
            self.phone_book.append(new)


    def save(self):
        data = []
        for contact in self.phone_book:
            data.append(':'.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def load(self):
        return self.phone_book
    def get_pb() -> list[dict[str, str]]:
        global phone_book
        return phone_book


    def add (self, new: dict[str, str]) -> str:
        self.last_id +=1
        new['id'] = str(new_id)
        self.phone_book.append(new)
        return new.get('name')

    def search(self, word:str) -> list[dict[str,str]]:
        result:list[dict[str,str]] = []
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lowr():
                    result.append(contact)
                    break
    def del_contact(index: int):
        return phone_book.pop(index - 1).get('name')


    def find_contact(name: str):
        global phone_book
        for contacts in phone_book:
            if name == contacts:
                return 'True'


my_pb =