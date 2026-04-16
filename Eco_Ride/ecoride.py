class EcoRideMain:
    @staticmethod
    def start():
        print("=" * 50)
        print(" Welcome to Eco-Ride Urban Mobility System ")
        print("=" * 50)


if __name__ == "__main__":
    EcoRideMain.start()



class Vehicle:
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


    def display(self):
        print("\n--- Vehicle Details ---")
        print("Vehicle ID      :", self.vehicle_id)
        print("Model           :", self.model)
        print("Battery (%)     :", self.__battery_percentage)
        print("Maintenance     :", self.__maintenance_status)
        print("Rental Price    : $", self.__rental_price)


v1 = Vehicle("KL-70A-0369", "BMW E5", 80)

v1.set_rental_price(500)
v1.set_maintenance_status("Excellent")

v1.display()

v1.set_battery(150)   