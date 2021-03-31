import AbstractProduct


class CreatePhone(AbstractProduct.AbstractProduct):
    def __init__(self, title):
        self.title = title
        self.type = 'phone'

    @property
    def get_title(self):
        return self.title

    @property
    def get_type(self):
        return self.type
