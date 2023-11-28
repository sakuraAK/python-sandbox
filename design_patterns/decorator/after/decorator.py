from abc import ABC, abstractmethod
from coffee import Coffee


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    @property
    def coffee(self):
        return self._coffee