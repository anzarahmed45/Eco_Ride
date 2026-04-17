from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter

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


    def search_by_hub(self, hub_name):
        if hub_name in self.fleet_hubs:
            print(f"\nVehicles in Hub: {hub_name}")
            for v in self.fleet_hubs[hub_name]:
                print(f"  - {v.vehicle_id} | {v.model} | Battery: {v.get_battery()}%")
        else:
            print(f"Hub '{hub_name}' not found.")

    def search_high_battery(self, threshold=80):
        print(f"\nVehicles with Battery > {threshold}%:")

        all_vehicles = [v for vehicles in self.fleet_hubs.values() for v in vehicles]

        result = list(filter(lambda v: v.get_battery() > threshold, all_vehicles))

        if result:
            for v in result:
                print(f"  - {v.vehicle_id} | {v.model} | Battery: {v.get_battery()}%")
        else:
            print("No vehicles found with high battery.")

    def categorize_vehicles(self):
        categorized = {
            "Car": [],
            "Scooter": []
        }

        for vehicles in self.fleet_hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categorized["Car"].append(v)
                elif isinstance(v, ElectricScooter):
                    categorized["Scooter"].append(v)

        print("\n========== CATEGORIZED VEHICLES ==========")

        print("\nCars:")
        if categorized["Car"]:
            for v in categorized["Car"]:
                print(f"  - {v.vehicle_id} | {v.model}")
        else:
            print("  No cars available")

        print("\nScooters:")
        if categorized["Scooter"]:
            for v in categorized["Scooter"]:
                print(f"  - {v.vehicle_id} | {v.model}")
        else:
            print("  No scooters available")


    def vehicle_status_count(self):
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for hub in self.fleet_hubs:
            for v in self.fleet_hubs[hub]:
                status = v.get_maintenance_status()

                if status in status_count:
                    status_count[status] += 1

        print("\n====== Fleet Status Summary ======")
        for status in status_count:
            print(f"{status}: {status_count[status]}")

    def sort_by_model(self, hub_name):
        if hub_name in self.fleet_hubs:
            vehicles = self.fleet_hubs[hub_name]

            sorted_list = sorted(vehicles, key=lambda v: v.model)

            print(f"\n====== Vehicles in {hub_name} (Sorted by Model) ======")
            for v in sorted_list:
                print(v)   # uses __str__()
        else:
            print(f"Hub '{hub_name}' not found.")
