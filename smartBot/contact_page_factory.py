from abc import abstractmethod, ABC

from contact_page import UserPreview, AllDataPreview, ContactsPreview, ContactPreview


class AbstractUserPreviewFactory(ABC):
    @abstractmethod
    def create_simple_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_contacts_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_contact_preview(self) -> UserPreview:
        pass


class UserPreviewFactory(AbstractUserPreviewFactory):

    def create_simple_preview(self) -> AllDataPreview:
        return AllDataPreview()

    def create_contacts_preview(self) -> ContactsPreview:
        return ContactsPreview()

    def create_contact_preview(self) -> ContactPreview:
        return ContactPreview()
