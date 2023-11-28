from abc import ABC, abstractmethod

class Adapter(ABC):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee


    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def address(self):
        pass