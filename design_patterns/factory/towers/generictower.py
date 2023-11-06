from .towerinterface import TowerInterface
class GenericTower(TowerInterface):

    def __init__(self, name):
        self._name = name
    def fire(self):
        print(f"{self._name} is unknown type of tower")

    def take_damage(self):
        pass