class DoctorService:
    def __init__(self, datastore):
        self.datastore = datastore

    def add_doctor(self, doctor):
        # Store the full Doctor object so main.py can pass a model instance directly.
        doctor_id = doctor.id
        if doctor_id in self.datastore["doctors"]:
            raise ValueError("Doctor with this ID already exists.")
        self.datastore["doctors"][doctor_id] = doctor

    def get_doctor(self, doctor_id):
        doctor = self.datastore["doctors"].get(doctor_id, None)
        if doctor:
            return doctor.display_info()
        return None
    
    def update_doctor(self, doctor_id, doctor_name):
        if doctor_id in self.datastore["doctors"]:
            # Update only the name to keep the change minimal.
            self.datastore["doctors"][doctor_id].name = doctor_name
            return True
        return False
    
    def delete_doctor(self, doctor_id):
        if doctor_id in self.datastore["doctors"]:
            del self.datastore["doctors"][doctor_id]
            return True
        return False
    
    