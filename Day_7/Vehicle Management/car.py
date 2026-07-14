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


