from adapter import Adapter


class VendorAdapter(Adapter):
    def name(self):
        return self.adaptee.name

    def address(self):
        return f'{self.adaptee.number} {self.adaptee.street}'
