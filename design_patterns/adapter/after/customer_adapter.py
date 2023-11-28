from adapter import Adapter

class CustomerAdapter(Adapter):

    def name(self):
        return self.adaptee.name

    def address(self):
        return self.adaptee.address
