class Position():
    position_name = ""

    def __init__(self, position_name):
        self.position_name = position_name

class Worker(Position):
    name = ""
    surname = ""
    __income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = Position(position);
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self.__income.values())


if __name__ == '__main__':
    worker = Worker("Иван", "Иванов", "Директор", 100000, 50000)
    print(worker.get_full_name())
    print(worker.get_total_income())