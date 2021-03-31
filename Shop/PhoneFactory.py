import AbstractItemFactory, CreatePhone


class PhoneFactory(AbstractItemFactory.AbstractItemFactory):
    @staticmethod
    def create_phone(title):
        return CreatePhone.CreatePhone(title)


A = PhoneFactory()
b = A.create_phone('samsung')
print(b.get_title, b.get_type)