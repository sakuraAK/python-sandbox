from abc import ABC, abstractmethod

class TowerInterface(ABC):
    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def take_damage(self):
        pass
