import string
import abc

class Vehicle(abc.ABC):
    @abc.abstractmethod
    def start(self):
        """

        :return:
        """
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def go_forward(self, speed, accel):
        pass

    @abc.abstractmethod
    def go_backward(self, speed, accel):
        pass

class PassengerVehicle(abc.ABC):

    @abc.abstractmethod
    def load_passengers(self, num_of_pass):
        pass

    @abc.abstractmethod
    def unload_passengers(self, num_of_pass):
        pass


class Car(Vehicle):

    def start(self):
        print("Car start")

    def stop(self):
        print("Car is stopping")

    def go_forward(self, speed, accel):
        pass

    def go_backward(self, speed, accel):
        pass

class Convertible(Car):
    def start(self):
        print("Conv start")


class Bus(Vehicle, PassengerVehicle):
    def start(self):
        print("Bus start")

    def stop(self):
        print("Bus is stopping")

    def go_forward(self, speed, accel):
        pass

    def go_backward(self, speed, accel):
        pass

    def load_passengers(self, num_of_pass):
        print(f"Bus loads {num_of_pass} passengers")

    def unload_passengers(self, num_of_pass):
        print(f"Bus unloads {num_of_pass} passengers")

class Truck(Vehicle):
    def start(self):
        print("Truck start")

    def stop(self):
        print("Truck is stopping")

    def go_forward(self, speed, accel):
        pass

    def go_backward(self, speed, accel):
        pass

c = Bus()
# c.start()
# c.stop()

fleet = [Car(), Convertible(), Truck(), Bus()]

for v in fleet:
    if isinstance(v, Vehicle):
        v.start()
    if isinstance(v, PassengerVehicle):
        v.load_passengers(5)
        v.unload_passengers(10)
class Car:
    def __init__(self, make, model, year, max_speed):
        self._make = make
        self._model = model
        self._year = year
        self._speed = 0
        self._engine = "off"
        self._max_speed = max_speed


    def get_information(self):
        print(f"The make: {self._make} \nThe model:{self._model} \n"
              f"The year: {self._year}\n"
              f"The current speed: {self._speed} mph")
        # print("The make: " + self.make)
        # print("The make: {0} {0}".format(self.make))

    def drive(self):
        self._engine = "on"

    def stop(self):
        self._speed = 0

    def set_speed(self, speed):
        if speed < 0:
            return

        if speed > self._max_speed:
            self._speed = self._max_speed
        else:
            self._speed = speed


new_car = Car(model="Impreza", make="Subaru", year="2023", max_speed=140)
new_car.set_speed(1000)
new_car.get_information()

class Car(abc.ABC):

    def __init__(self, make, model, year, max_speed):
        self._make = make
        self._model = model
        self._year = year
        self._speed = 0
        self._engine = "off"
        self._max_speed = max_speed

    @abc.abstractmethod
    def get_information(self):
        pass
        # print(f"The make: {self._make} \nThe model:{self._model} \n"
        #       f"The year: {self._year}\n"
        #       f"The current speed: {self._speed} mph\n"
        #       f"The number of seats: {self._capacity}")
        # print("The make: " + self.make)
        # print("The make: {0} {0}".format(self.make))

    def drive(self, ):
        self._engine = "on"

    def stop(self):
        self._speed = 0

    def set_speed(self, speed):
        if speed < 0:
            return

        if speed > self._max_speed:
            self._speed = self._max_speed
        else:
            self._speed = speed


class TwoDoorCar(Car):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year, max_speed)
        self._capacity = 2

    # def get_information(self):
    #     print(f"The make: {self._make} \nThe model:{self._model} \n"
    #             f"The year: {self._year}\n"
    #             f"The current speed: {self._speed} mph\n"
    #             f"The number of seats: {self._capacity}")


class SedanCar(Car):
    pass
    # def get_information(self):
    #     print(f"The make: {self._make} \nThe model:{self._model} \n"
    #       f"The year: {self._year}\n"
    #       f"The current speed: {self._speed} mph\n")


# new_car = Car(model="Impreza", make="Subaru", year="2023",
#               max_speed=140)
new_car = SedanCar(model="Impreza", make="Subaru", year="2023",
                   max_speed=140)
# new_car.set_speed(1000)
new_car.get_information()

