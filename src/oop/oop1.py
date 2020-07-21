# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# This is the base class
class Vehicle:
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Base Class
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass
        
    # Airplane's parent is Flight Vehicle
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# Base Class
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
