from abc import ABC, abstractmethod
from .house_1 import House

class HouseBuilderInterface(ABC):

    def __init__(self):
        self.new_house()
    def get_house(self) -> House:
        return self._house

    def new_house(self):
        self._house = House()

    @abstractmethod
    def prep_foundation(self):
        pass

    @abstractmethod
    def construct_walls(self):
        pass

    @abstractmethod
    def install_windows(self):
        pass

    @abstractmethod
    def put_roof(self):
        pass

    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def do_interior(self):
        pass

    @abstractmethod
    def add_garage(self):
        pass