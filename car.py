class Odometer:
    def __init__(self, odometer=0):
        self.odometer = odometer
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    try:
        def describe_battery(self):
        #Print a statement describing the battery size.
            print(f"This car has a {self.battery_size}-kWh battery.")
    except AttributeError:
        print('refe')
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = Odometer()
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.odometer = Odometer()


my_new_car = Car('BMW', 'gtr', '2009')
print(my_new_car.get_descriptive_name())
my_new_car.odometer.odometer_reading = 80
my_new_car.odometer.read_odometer()

