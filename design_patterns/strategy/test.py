from shippers import FedexShipping, UPSShipping, CanadaPostShipping
from order import Order
from shipping_cost import ShippingCostCalc


if __name__ == "__main__":
    shipping_strategy = CanadaPostShipping()
    calc = ShippingCostCalc(shipping_strategy)
    order = Order()
    print(calc.strategy.calculate(order))