from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def description(self):
        pass
    @abstractmethod
    def cost(self):
        pass