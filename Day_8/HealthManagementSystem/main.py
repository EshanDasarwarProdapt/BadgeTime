from data.datastore import datastore
from models.patient import Patient
from services.healthcare_system import HealthcareSystem

system = HealthcareSystem(datastore)

p1 = Patient(1, "John Doe", 30, "Flu")
p2 = Patient(2, "Jane Smith", 25, "Cold")

system.patient_service.add_patient(p1)
system.patient_service.add_patient(p2)

print(system.patient_service.get_patient(2))