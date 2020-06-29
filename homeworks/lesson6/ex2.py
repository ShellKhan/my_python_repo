class Road:
    ASPHALT_WEIGHT = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, quality):
        return self._length * self._width * self.ASPHALT_WEIGHT * quality / 1000

m11_road = Road(650000, 50)
print(m11_road.calculation(5))
test_road = Road(5000, 20)
print(test_road.calculation(5))