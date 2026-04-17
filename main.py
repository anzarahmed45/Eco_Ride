from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter
from services.fleet_manager import FleetManager

class EcoRideMain:
    @staticmethod
    def start():
        print("=" * 50)
        print(" Welcome to Eco-Ride Urban Mobility System ")
        print("=" * 50)


if __name__ == "__main__":
    EcoRideMain.start()


manager = FleetManager()

car1 = ElectricCar("KL-70A-0369", "BMW E5", 85, 5)
car2 = ElectricCar("KL-70B-0456", "Mercedez E7", 70, 5)
scooter1 = ElectricScooter("KL-70B-0369", "Ather 450X", 90, 90)

manager.add_hub("Downtown")

manager.add_vehicle("Downtown", car1)
manager.add_vehicle("Downtown", car2)
manager.add_vehicle("Downtown", scooter1)

manager.sort_by_model("Downtown")