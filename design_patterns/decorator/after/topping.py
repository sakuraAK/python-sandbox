from decorator import CoffeeDecorator


class WhippedCream(CoffeeDecorator):

    def description(self):
        return self.coffee.description() + ", Whipped cream topping"

    def cost(self):
        return self.coffee.cost() + 0.2


class Cinnamon(CoffeeDecorator):

    def description(self):
        return self.coffee.description() + ", Cinnamon topping"

    def cost(self):
        return self.coffee.cost() + 0.1
