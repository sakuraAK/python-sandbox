import sys
sys.path.append('C:\\Users\\andre\\dev\\python-sandbox\\design_patterns\\decorator')
import milk, topping, flavour
from before import ArabicaCoffee, RobustaCoffee, Coffee





def make(coffee: Coffee):
    print(f"Desc: {coffee.description()}, Cost: {coffee.cost()}$")


def main():
    coffee = ArabicaCoffee()
    make(coffee)
    coffee = milk.OatMilkDecorator(coffee)
    make(coffee)
    coffee = milk.SoyaMilk(coffee)
    make(coffee)
    coffee = flavour.IrishCreamFlavour(coffee)
    make(coffee)
    coffee = topping.WhippedCream(coffee)
    make(coffee)
    coffee = topping.Cinnamon(coffee)
    make(coffee)




main()