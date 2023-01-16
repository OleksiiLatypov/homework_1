from abc import abstractmethod, ABC


class UserPreview(ABC):
    @abstractmethod
    def build_preview(self, data):
        pass


class AllDataPreview(UserPreview):
    def build_preview(self, data):
        return data


class ContactsPreview(UserPreview):
    def build_preview(self, data):
        contacts = ''
        page_number = 1
        for page in data.iterator():
            contacts += f'Page# {page_number}\n'
            for record in page:
                contacts += f'{record.get_info()}\n'
        return contacts


class ContactPreview(UserPreview):
    def build_preview(self, data):
        birthday_info = ''
        email_info = ''
        address_info = ''
        notes_info = ''
        phones_info = ','.join([phone.value for phone in data.phones])

        if data.birthday:
            birthday_info += f'{data.birthday.value}'

        if data.email:
            email_info += f'Birthday: {data.email.value}'

        if data.address:
            address_info += f'Address: {data.address.value}'

        if data.notes:
            notes_info += f'Notes: {data.notes.value}'

        return f'{data.name.value}: {phones_info}, {email_info}, {address_info}, {notes_info}'









