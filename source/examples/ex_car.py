# There's no single right answer here. This is just an example.

class Car:
    def __init__(self, name, make, model, year, value):
        self.name = name
        self.make = make
        self.model = model
        self.year = year
        self.value = value
        self.location = None

    def honk(self):
        print("Beep beep!")

    def drive_to(self, destination):
        print(f'Welcome to {destination}!')
        self.location = destination

    def rename(self, name):
        self.name = name

    def total(self):
        print("Oh noes!")
        self.value = 0
