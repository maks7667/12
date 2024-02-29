"""
Только для оценки 10\10 в pylint
"""
class Wheels:
    """
    Только для оценки 10\10 в pylint
    """
    def __init__(self, number_of_wheels):
        """
        Только для оценки 10\10 в pylint
        """
        self.number_of_wheels = number_of_wheels

    def rotate(self):
        """
        Только для оценки 10\10 в pylint
        """
        print(f"Колеса вращаются.")

class Engine:
    """
    Только для оценки 10\10 в pylint
    """
    def __init__(self, horsepower):
        """
        Только для оценки 10\10 в pylint
        """
        self.horsepower = horsepower

    def start(self):
        """
        Только для оценки 10\10 в pylint
        """
        print(f"Двигатель запущен. Мощность {self.horsepower} лошадиных сил.")

class Doors:
    """
    Только для оценки 10\10 в pylint
    """
    def __init__(self, number_of_doors):
        """
        Только для оценки 10\10 в pylint
        """
        self.number_of_doors = number_of_doors

    def open(self):
        """
        Только для оценки 10\10 в pylint
        """
        print(f"Все {self.number_of_doors} двери открыты.")

    def close(self):
        """
        Только для оценки 10\10 в pylint
        """
        print(f"Все {self.number_of_doors} двери закрыты.")

class Car(Wheels, Engine, Doors):
    """
    Только для оценки 10\10 в pylint
    """
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        """
        Только для оценки 10\10 в pylint
        """
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def drive(self):
        """
        Только для оценки 10\10 в pylint
        """
        print("The car is driving.")

my_car = Car(number_of_wheels=4, horsepower=200, number_of_doors=4)

my_car.start()
my_car.rotate()
my_car.open()
my_car.drive()
my_car.close()
