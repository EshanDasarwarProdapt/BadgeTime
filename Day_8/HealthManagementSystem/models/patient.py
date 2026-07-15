from person import Person

class Patient(Person):
    def __init__(self, id, name, age, ailment):
        super().__init__(id, name, age)
        self.ailment = ailment

    def display_info(self):
        details = super().display_info()
        details.update({"ailment": self.ailment})
        return details
    

a = Patient(1, "John Doe", 30, "Flu")
print(a.display_info())