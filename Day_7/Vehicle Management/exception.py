class VehicleError(Exception):
    """Base class for exceptions in this module."""
    pass

class OwnerAlreadyExistsError(VehicleError):
    """Exception raised when trying to set an owner that already exists."""
    def __init__(self, owner_name):
        message = f"Owner '{owner_name}' already exists. Use change_owner method to change the owner."
        super().__init__(message)

class InvalidBatteryCapacityError(VehicleError):
    """Exception raised for invalid battery capacity values."""
    def __init__(self,capacity):
        message = f"Invalid battery capacity: {capacity}. Battery capacity must be a positive number."
        super().__init__(message)