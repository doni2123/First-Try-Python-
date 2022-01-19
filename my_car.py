from car import * 
my_new_car = Car('BMW', 'gtr', '2009')
print(my_new_car.get_descriptive_name())
my_new_car.odometer.odometer_reading = 80
my_new_car.odometer.read_odometer()
