from strategy import AbsStrategy

class ShippingCostCalc:

    def __init__(self, strategy: AbsStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy