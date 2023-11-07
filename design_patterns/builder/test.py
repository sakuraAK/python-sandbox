from first_try.house import House
from builder_pattern.engineer import Engineer
from builder_pattern.house_builder import StandardHouseBuilder, StandardHouseWithGarageBuilder, \
    IglooBuilder
def builder_test():
    house_builder = Engineer(StandardHouseBuilder())
    house_builder.build()
    house_builder.get_house().display()

    house_builder = Engineer(StandardHouseWithGarageBuilder())
    house_builder.build()
    house_builder.get_house().display()

    house_builder = Engineer(IglooBuilder())
    house_builder.build()
    house_builder.get_house().display()
def first_try_test():
    house = House(roof="Shingles",
                  walls="Red bricks",
                  windows="White vinyl double",
                  interior="Farmhouse",
                  basement="Finished",
                  foundation="Reinforced concrete")
    house.display()

if __name__ == "__main__":
    # first_try_test()
    builder_test()
