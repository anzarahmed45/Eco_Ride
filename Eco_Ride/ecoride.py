from abc import ABC, abstractmethod

class EcoRideMain:
    @staticmethod
    def start():
        print("=" * 50)
        print(" Welcome to Eco-Ride Urban Mobility System ")
        print("=" * 50)


if __name__ == "__main__":
    EcoRideMain.start()



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


class FleetManager:
    def __init__(self):
        self.fleet_hubs = {}   

    def add_hub(self, hub_name):
        if hub_name not in self.fleet_hubs:
            self.fleet_hubs[hub_name] = []
            print(f"Hub '{hub_name}' added.")
        else:
            print(f"Hub '{hub_name}' already exists.")

    def add_vehicle(self, hub_name, vehicle):
            if hub_name in self.fleet_hubs:
                if any(v.vehicle_id == vehicle.vehicle_id for v in self.fleet_hubs[hub_name]):
                    print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in {hub_name}.")
                else:
                    self.fleet_hubs[hub_name].append(vehicle)
                    print(f"Vehicle {vehicle.vehicle_id} added to {hub_name}.")
            else:
                print(f"Hub '{hub_name}' not found.")

    def display_hubs(self):
        print("\n========== FLEET HUBS ==========")
        for hub, vehicles in self.fleet_hubs.items():
            print(f"\nHub: {hub}")
            if not vehicles:
                print("  No vehicles available")
            else:
                for v in vehicles:
                    print(f"  - {v.vehicle_id} | {v.model}")


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5 + (0.5 * distance)

    def display(self):
        super().display()
        print("Type            : Car")
        print("Seating Capacity:", self.seating_capacity)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes):
        return 1 + (0.15 * minutes)

    def display(self):
        super().display()
        print("Type            : Scooter")
        print("Max Speed Limit :", self.max_speed_limit)


manager = FleetManager()

car1 = ElectricCar("KL-70A-0369", "BMW E5", 80, 5)
car2 = ElectricCar("KL-70A-0369", "Mercedez E7", 70, 5)

manager.add_hub("Downtown")

manager.add_vehicle("Downtown", car1)
manager.add_vehicle("Downtown", car2)  

manager.display_hubs()
