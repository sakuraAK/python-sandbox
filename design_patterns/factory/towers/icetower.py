from .towerinterface import TowerInterface

class IceTower(TowerInterface):

    def fire(self):
        print("Ice tower is firing")


    def take_damage(self):
        print("Ice tower takes damage")