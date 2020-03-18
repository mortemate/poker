class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        print("Run is " + str(self.odometer_reading) + " km")

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Don't try to fuck others, jerk")

    def increment_odometer(self, km):
        if km > 0:
            self.odometer_reading += km
        else:
            print("WTH r u doing, little piece of shit!?!!?!?")

auto = Car("Audi", "a4", 2017)
#auto.odometer_reading = 30
#auto.update_odometer(20)
#auto.update_odometer(10)

auto.increment_odometer(-15)
auto.update_odometer(12)

auto.read_odometer()
