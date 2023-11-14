from inspect import isclass
from store import Store
from customer import AndroidFan, AppleFan

# class Store:
#     _iphone_price = 1800
#     _samsung_price = 1500
#     _pixel_price = 2000
#
#     @property
#     def iphone_price(self):
#         return self._iphone_price
#
#     @property
#     def samsung_price(self):
#         return self._samsung_price
#
#     @property
#     def pixel_price(self):
#         return self._pixel_price
#
#     def update_price(self, brand, new_price):
#         if brand == "iphone":
#             self._iphone_price = new_price
#         elif brand == "samsung":
#             self._samsung_price = new_price
#         elif brand == "pixel":
#             self._pixel_price = new_price
#         else:
#             raise ValueError("Unsupported brand")
#
#
# class IphoneFan:
#     _max_price = 1500
#
#     @property
#     def max_price(self):
#         return self._max_price
#
#
#     def buy(self):
#         print(f"{self.__class__.__name__} - Hooray")
#
#
# class AndroidUser:
#     _max_price = 1200
#
#     @property
#     def max_price(self):
#         return self._max_price
#
#     def buy(self):
#         print(f"{self.__class__.__name__} - Hooray")



if __name__ == "__main__":
    store = Store()

    # c1 = AndroidFan(store)
    # store.attach(c1)
    # c2 = AppleFan(store)
    # store.attach(c2)
    #
    # store.set_price("iphone", 2000)
    # store.set_price("samsung", 2000)
    # store.set_price("pixel", 1000)
    with AndroidFan(store) as c1, AppleFan(store) as c2:
        store.attach(c1)
        c2 = AppleFan(store)
        store.attach(c2)

        store.set_price("iphone", 2000)
        store.set_price("samsung", 2000)
        store.set_price("pixel", 1000)
    import sys
    print(sys.getrefcount(c1))


    # clients = [IphoneFan(), AndroidUser()]
    #
    # store.update_price("pixel", 1000)
    #
    # for client in clients:
    #     if isinstance(client, IphoneFan):
    #         if store.iphone_price <= client.max_price:
    #             client.buy()
    #     elif isinstance(client, AndroidUser):
    #         if store.pixel_price <= client.max_price \
    #                 or store.samsung_price <= client.max_price:
    #             client.buy()

