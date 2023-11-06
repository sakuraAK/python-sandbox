from .towerinterface import TowerInterface

class ArcherTower(TowerInterface):
    def fire(self):
        print("Tower shooting arrows...")

    def take_damage(self):
        print("Archer tower taking damage...")