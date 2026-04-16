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
        self.battery_percentage = battery_percentage

    def display(self):
        print("\n--- Vehicle Details ---")
        print("Vehicle ID      :", self.vehicle_id)
        print("Model           :", self.model)
        print("Battery (%)     :", self.battery_percentage)


v1 = Vehicle("KL-70A-0369", "BMW E5", 80)
v1.display()