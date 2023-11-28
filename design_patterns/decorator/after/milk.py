from decorator import CoffeeDecorator


class OatMilkDecorator(CoffeeDecorator):

    def description(self):
        return self.coffee.description() + ", Oat milk"

    def cost(self):
        return self.coffee.cost() + 1.5


class SoyaMilk(CoffeeDecorator):
    def description(self):
        return self.coffee.description() + ", Soya Milk"


    def cost(self):
        return self.coffee.cost() + 0.35

