class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f'{self.title} is drawing')

class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f'{self.title} is drawing')

class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print(f'{self.title} is drawing')

if __name__ == '__main__':
    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()