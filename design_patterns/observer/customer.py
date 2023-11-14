from observer import AbsObserver
from store import Store
class AppleFan(AbsObserver):
    _max_price = 1900

    def __init__(self, store: Store):
        self._store = store

    def update(self):
        if self._store.iphone_price <= self._max_price:
            print(f"{self.__class__.__name__} says: Hooray!")
        else:
            print(f"{self.__class__.__name__} says: Oooof!")


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._store.detach(self)

class AndroidFan(AbsObserver):
    _max_price = 1250

    def __init__(self, store: Store):
        self._store = store

    def update(self):
        if self._store.pixel_price <= self._max_price \
            or self._store.samsung_price <= self._max_price:
            print(f"{self.__class__.__name__} says: Hooray!")
        else:
            print(f"{self.__class__.__name__} says: Oooof!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._store.detach(self)