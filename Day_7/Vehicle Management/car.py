class Car:

    def __init__(self, brand, model, year, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner  # Private attribute

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started.")

    def show_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")
        print(f"Owner: {self.__owner}")

    def get_owner(self):
        return self.__owner  # Public method to access the private attribute
    def set_owner(self, new_owner):
        if self.__owner == None:
            self.__owner = new_owner  # Public method to modify the private attribute
        else:
            print(f"Owner {self.__owner} already set. Use change_owner method to change the owner.")

        
a = Car("Toyota", "Camry", 2020, "Mayur")  # Passing owner name as an argument

b = Car("Honda", "Civic", 2022, "Jane Smith")  # Passing owner name as an argument


print(a.brand)  # Output: Toyota
print(a.get_owner())  # Output: Mayur
a.set_owner("Alice Johnson")  # Changing the owner using the setter method
print(a.get_owner())  # Output: Alice Johnson

# l = [a, b]

# for car in l:
#     car.start_engine()
#     car.show_info()
