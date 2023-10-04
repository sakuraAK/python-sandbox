import abc
class Person:
    def __init__(self, date_of_birth, name):
        self._date_of_birth = date_of_birth
        self._name = name

    def get_age(self) -> int:
        pass

    def _get_years_from_dob(self):
        pass

class Car:
    def __init__(self):
        self._mileage = 0
        self._units = "imperial"
        self._current_speed = 0

    def _get_mileage_reading(self):
        if self._units == "metric":
            return int(self._mileage * 1.6)
        return self._mileage

    def toggle_units(self):
        if self._units == "metric":
            self._units = "imperial"
        else:
            self._units = "metric"

    def set_current_speed(self, speed):
        if speed < 0:
            return
        self._current_speed = speed

    def get_mileage(self):
        return self._get_mileage_reading()

class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    def calc_area(self):
        return 3.14 * (self._radius ** 2)


class ResizableCircle(Circle):

     # def __init__(self, radius, ratio):
     #     super().__init__(radius)
     #     self._ratio = ratio
    def resize(self, ratio: float):
        self._radius *= ratio


circle1 = Circle(5)
circle2 = ResizableCircle(5)
print(f"Area of circle 1: {circle1.calc_area()}"
      f"\nArea of circle 2: {circle2.calc_area()}")
circle2.resize(0.5)
print(f"Area of circle 1: {circle1.calc_area()}"
      f"\nArea of circle 2: {circle2.calc_area()}")


# implementation of instance counter using static member

# implementation of static utility function

# example of method overloading

class Adder:

    def add(self, a: int):
        return a + a
    def add(self, a: int, b: int):
        return  a + b

    def add(self, a:str, b:str):
        return a + b

    def add(self, x: complex, y: complex):
        return complex(x.real + y.real, y.imag + x.imag)


# example of method overriding

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
     def make_sound(self):
         print("Woof")


class Duck(Animal):
    def make_sound(self):
        print("Quack")


class DoubleQuackDuck(Duck):
    def make_sound(self):
        super().make_sound()
        super().make_sound()

animal1 = Dog()
animal2 = Duck()
animal3 = DoubleQuackDuck()

animal1.make_sound()
animal2.make_sound()
animal3.make_sound()


# animal.make_sound()