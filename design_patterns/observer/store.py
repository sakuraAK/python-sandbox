from subject import AbsSubject

class Store(AbsSubject):
    _iphone_price = 2000
    _pixel_price = 1700
    _samsung_price = 1350

    @property
    def iphone_price(self):
        return self._iphone_price

    @property
    def pixel_price(self):
        return self._pixel_price

    @property
    def samsung_price(self):
        return self._samsung_price

    def set_price(self, brand, price):
        if brand == "iphone":
            self._iphone_price = price
        elif brand == "pixel":
            self._pixel_price = price
        elif brand == "samsung":
            self._samsung_price = price
        else:
            raise Exception("Unsupported brand")
        self.notify()