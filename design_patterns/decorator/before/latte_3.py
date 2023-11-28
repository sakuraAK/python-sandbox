from latte_milk_cinnamon import ArabicaPumpkinSpiceLatte


class ArabicaPumpkinSpiceAndCinnamonLatte(ArabicaPumpkinSpiceLatte):

    def description(self):
        return super().description() + ',Cinnamon topping'

    def cost(self):
        return super().cost() + 0.5



