class House(object):
    roof: str
    walls: str
    foundation: str
    basement: str
    windows: str
    interior: str
    garage = ""


    def display(self):
        print('Custom House:')
        print(f'\t{"Roof":>10}: {self.roof}')
        print(f'\t{"Walls":>10}: {self.walls}')
        print(f'\t{"Windows":>10}: {self.windows}')
        print(f'\t{"Interior":>10}: {self.interior}')
        print(f'\t{"Garage":>10}: {self.garage}')
        print(f'\t{"Basement":>10}: {self.basement}')
        print(f'\t{"Foundation":>10}: {self.foundation}')
