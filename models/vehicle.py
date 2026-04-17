from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = None
        self.__maintenance_status = "Good"
        self.__rental_price = 0

        self.set_battery(battery_percentage)


    def get_battery(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price


    def set_battery(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery percentage! (0-100 only)")

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_rental_price(self, rental_price):
        if rental_price >= 0:
            self.__rental_price = rental_price
        else:
            print("Rental price cannot be negative!")

    @abstractmethod
    def calculate_trip_cost(self, value):
        pass


    def display(self):
        print("\n--- Vehicle Details ---")
        print("Vehicle ID      :", self.vehicle_id)
        print("Model           :", self.model)
        print("Battery (%)     :", self.__battery_percentage)
        print("Maintenance     :", self.__maintenance_status)
        print("Rental Price    : $", self.__rental_price)


    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False
