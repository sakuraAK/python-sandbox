from towers.archertower import ArcherTower
from towers.cannontower import CannonTower
from towers.fireballtower import FireballTower
from towers.generictower import GenericTower
from tower_factory import TowerFactory

def tower_test_factory():
    factory = TowerFactory()
    for name in "ArcherTower", "CannonTower", "FireballTower", "IceTower":
        tower = factory.create_tower(name)
        tower.fire()
        tower.take_damage()



def tower_test_no_factory():
    for name in "ArcherTower", "CannonTower", "FireballTower", "IceTower":
        if name == "ArcherTower":
            tower = ArcherTower()
            tower.fire()
            tower.take_damage()
        elif name == "CannonTower":
            tower = CannonTower()
            tower.fire()
            tower.take_damage()
        elif name == "FireballTower":
            tower = FireballTower()
            tower.fire()
            tower.take_damage()
        else:
            tower = GenericTower(name)
            tower.fire()
            tower.take_damage()


if __name__ == "__main__":
    # tower_test_no_factory()
    # print('------------------------')
    tower_test_factory()

# To add Ice tower I will need to modify this code which breaks the open/closed prinicple
# We also instantiate concrete classes which breaks Dependency Inversion principle