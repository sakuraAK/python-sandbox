'''
Coffee
Base
Milk
Flavour
Topping
'''

from coffee import  Coffee
from  latte_3 import ArabicaPumpkinSpiceAndCinnamonLatte
from lattte_2 import RobustaPumpkinSpiceLatte

def make(coffee: Coffee):
    print(f"Desc: {coffee.description()}, Cost: {coffee.cost()}$")

def main():
    coffee = ArabicaPumpkinSpiceAndCinnamonLatte()
    make(coffee)
    coffee = RobustaPumpkinSpiceLatte()
    make(coffee)


main()