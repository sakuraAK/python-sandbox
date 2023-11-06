from inspect import getmembers, isclass, isabstract
import towers
from towers.towerinterface import TowerInterface
from towers.generictower import GenericTower

class TowerFactory:
    def __init__(self):
        self._towers = {}
        self.load_towers()

    def load_towers(self):
        classes = getmembers(towers, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, TowerInterface):
                self._towers.update([[name, _type]])

    def create_tower(self, name) -> TowerInterface:
        if name in self._towers:
            return self._towers[name]()
        else:
            return GenericTower(name)
