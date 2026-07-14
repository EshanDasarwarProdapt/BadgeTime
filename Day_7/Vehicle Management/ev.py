from car import Car
from exception import InvalidBatteryCapacityError

class EV(Car):
    def __init__(self, brand, model, year, battery_capacity, owner = None):
        super().__init__(brand, model, year, owner)  # Call the parent class constructor
        if battery_capacity <= 0:
            raise InvalidBatteryCapacityError(battery_capacity)
        else: 
            self.battery_capacity = battery_capacity  # kWh

    def charge_battery(self):
        print(f"Charging the {self.brand} {self.model} battery ({self.battery_capacity} kWh)...")

    def show_info(self):
        super().show_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        

    def start_engine(self):
        print(f"The {self.brand} {self.model} electric engine has started silently.")

    def charge_battery(self):
        print(f"The {self.brand} {self.model} is charging its {self.battery_capacity} kWh battery.")