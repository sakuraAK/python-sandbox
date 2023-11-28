from arabica import ArabicaCoffee


class ArabicaPumpkinSpiceLatte(ArabicaCoffee):

    def description(self):
        return super().description() + ', Milk, Pumpkin Spice topping'

    def cost(self):
        return super().cost() + 1.35



