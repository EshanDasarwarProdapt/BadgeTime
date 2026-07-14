from car import Car
from ev import EV
from polymorphism import Overloadingdemo
from polymorphism import overloading

overloading()


a = Car("Toyota", "Camry", 2020, "Mayur")  # Passing owner name as an argument

b = Car("Honda", "Civic", 2022, "Jane Smith")  # Passing owner name as an argument

ev1 = EV("Tesla", "Model3", 2021, 75)

# ev1.show_info()
# a.start_engine()
# ev1.charge_battery()


# print(a.brand)  # Output: Toyota
# print(a.get_owner())  # Output: Mayur
# a.set_owner("Alice Johnson")  # Changing the owner using the setter method
# print(a.get_owner())  # Output: Alice Johnson

# l = [a, b]

# for car in l:
#     car.start_engine()
#     car.show_info()
