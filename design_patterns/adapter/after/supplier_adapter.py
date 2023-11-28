from adapter import Adapter

class SupplierAdapter(Adapter):

    def name(self):
        return f'{self.adaptee.first_name} {self.adaptee.last_name}'

    def address(self):
        return self.adaptee.address
