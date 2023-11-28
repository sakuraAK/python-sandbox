from robusta import  RobustaCoffee


class RobustaPumpkinSpiceLatte(RobustaCoffee):

    def description(self):
        return super().description() + ', Milk, Pumpkin Spice topping'

    def cost(self):
        return super().cost() + 1.35



