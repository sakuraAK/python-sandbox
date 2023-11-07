class House(object):

    def __init__(self, roof, walls, foundation, basement, windows, interior):
        self.roof = roof
        self.walls = walls
        self.foundation = foundation
        self.basement = basement
        self.windows = windows
        self.interior = interior

    def display(self):
        print('Custom House:')
        print(f'\t{"Roof":>10}: {self.roof}')
        print(f'\t{"Walls":>10}: {self.walls}')
        print(f'\t{"Windows":>10}: {self.windows}')
        print(f'\t{"Interior":>10}: {self.interior}')
        print(f'\t{"Basement":>10}: {self.basement}')
        print(f'\t{"Foundation":>10}: {self.foundation}')