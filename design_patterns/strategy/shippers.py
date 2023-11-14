from strategy import AbsStrategy


class UPSShipping(AbsStrategy):

    def calculate(self, order):
        return 5


class FedexShipping(AbsStrategy):

    def calculate(self, order):
        return 10


class CanadaPostShipping(AbsStrategy):
    def calculate(self, order):
        return 3