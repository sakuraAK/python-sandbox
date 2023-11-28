from decorator import CoffeeDecorator



class HazelnutFlavour(CoffeeDecorator):
    def description(self):
        return self.coffee.description() + ", Hazelnut flavour"

    def cost(self):
        return self.coffee.cost() + 0.5


class IrishCreamFlavour(CoffeeDecorator):
    def description(self):
        return self.coffee.description() + ", Irish cream flavour"

    def cost(self):
        return self.coffee.cost() + 0.75