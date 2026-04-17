from models.vehicle import Vehicle

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