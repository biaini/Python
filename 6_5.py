class Stationery:
    def __init__(self, title="Let's start:"):
        self.title = title

    def draw(self):
        print(f"Starting drawing! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Drawing with {self.title} is a pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Drawing with {self.title} is a pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Drawing with {self.title} is a marker!")


stat = Stationery()
pen = Pen("Bic")
pencil = Pencil("MOSKVA")
marker = Marker("Zebra")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()
