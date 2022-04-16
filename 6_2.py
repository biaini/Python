class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} sm =" \
               f" {(self._length * self._width * weight * thickness) / 1000} t"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())
