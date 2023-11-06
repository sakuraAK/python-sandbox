from .towerinterface import TowerInterface
class FireballTower(TowerInterface):
    def fire(self):
        print("Fire tower goes: Whooshhhh")

    def take_damage(self):
        print("Fireball tower taking damage...")