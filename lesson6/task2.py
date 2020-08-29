class Road:
    __length = 0
    __width = 0
    __kg_per_sm = 25

    def __init__(self, length, width):
        self.__length = float(length)
        self.__width = float(width)

    def weight(self, sm=1):
        return self.__length * self.__width * self.__kg_per_sm * sm / 1000

if __name__ == '__main__':
    road = Road(5000, 20)
    print(road.weight(5))