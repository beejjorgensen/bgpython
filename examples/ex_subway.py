class SubwayCar:
    """Information about a single subway car"""

    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        return self.name

head = SubwayCar("Engine")
car1 = SubwayCar("Passenger car 1")
car2 = SubwayCar("Passenger car 2")
car3 = SubwayCar("Passenger car 3")

# Hook all the cars together
head.next = car1
car1.next = car2
car2.next = car3
car3.next = None   # End of the train

# We start at the head of the train
location = head

# Walk along the train until the end
while location is not None:
    print(location)
    location = location.next  # Move to the next car