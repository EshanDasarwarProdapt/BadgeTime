from services.patient_service import PatientService
from services.doctor_service import DoctorService

class HealthcareSystem:

    def __init__(self, datastore):
        self.patient_service = PatientService(datastore)
        self.doctor_service = DoctorService(datastore)