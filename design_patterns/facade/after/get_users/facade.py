import abc

class AbsFacade(abc.ABC):
    @abc.abstractmethod
    def get_users(self):
        pass
