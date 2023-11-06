from .towerinterface import TowerInterface
class CannonTower(TowerInterface):
    def fire(self):
        print("Canon tower does: Kaa-boom!")

    def take_damage(self):
        print("Cannon tower taking damage...")