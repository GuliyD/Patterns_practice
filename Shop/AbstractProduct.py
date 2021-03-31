import abc


class AbstractProduct(abc.ABC):
    @abc.abstractmethod
    def get_title(self):
        pass

    @abc.abstractmethod
    def get_type(self):
        pass
