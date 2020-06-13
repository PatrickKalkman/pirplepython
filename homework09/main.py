"""
Python Is Easy course @Pirple.com
Homework Assignment #9: Classes
Patrick Kalkman / patrick@simpletechture.nl

Details:

Create a class called "Vehicle" and methods that allow you to set the "Make",
"Model", "Year,", and "Weight".

The class should also contain a "NeedsMaintenance" boolean that defaults to
False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state
of a boolean isDriving to True.  It should have another method called "Stop"
that sets the value of isDriving to false.

Switching isDriving from true to false should increment the
"TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100,
then the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the TripsSinceMaintenance
to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a different
number of times. Then print out their values for Make, Model, Year,
Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle.
Add methods to the Planes class for Flying and Landing
(similar to Driving and Stopping), but different in one respect:
Once the NeedsMaintenance boolean gets set to true, any attempt at flight
should be rejected (return false), and an error message should be printed
saying that the plane can't fly until it's repaired.


"""


class Vehicle:

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight


class Cars(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True
        self.isDriving = False

    def Repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

    def __str__(self):
        return (f"The {self.make} {self.model} which weighs {self.weight}"
                f" from {self.year} has {self.tripsSinceMaintenance} trips"
                f" and needs maintenance = {self.needsMaintenance}")


def drive(carToDrive, numberOfDrives):
    for _ in range(numberOfDrives):
        carToDrive.Drive()
        carToDrive.Stop()


porsche = Cars("Porsche", "911", "2020", "900 Kg")
ferrari = Cars("Ferrari", "812 GTS", "2020", "1100 Kg")
lambo = Cars("Lamborghini", "AVENTADOR S", "2020", "912 Kg")

drive(porsche, 11)
drive(ferrari, 121)
drive(lambo, 56)

print(porsche)
print(ferrari)
print(lambo)


class Planes(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlighing = False

    def Fly(self):
        if not self.needsMaintenance:
            self.isFlighing = True
        else:
            print("Sorry, this plane can't fly until it has been repaired")

    def Land(self):
        if self.isFlighing:
            self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True
        self.isFlighing = False

    def Repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

    def __str__(self):
        return (f"The {self.make} {self.model} which weighs {self.weight}"
                f" from {self.year} has {self.tripsSinceMaintenance} trips"
                f" and needs maintenance = {self.needsMaintenance}")


def fly(planeToFly, numberOfFlights):
    for _ in range(numberOfFlights):
        planeToFly.Fly()
        planeToFly.Land()


boeing = Planes("Boeing", "747", "2001", "183520 kg")
# check to see that we can fly the plane
boeing.Fly()
boeing.Land()
# fly the plane an additional 99 times
fly(boeing, 100)
# try to fly another time, it should give an error message
boeing.Fly()
# print the details of the plane
print(boeing)
