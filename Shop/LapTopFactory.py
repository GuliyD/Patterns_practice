import AbstractItemFactory, CreateLaptop


class LapTopFactory(AbstractItemFactory.AbstractItemFactory):
    @staticmethod
    def create_laptop(title):
        return CreateLaptop.CreateLaptop(title)



A = LapTopFactory()
b = A.create_laptop('HP')
print(b.get_title, b.get_type)