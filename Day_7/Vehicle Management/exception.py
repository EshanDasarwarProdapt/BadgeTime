class VehicleError(Exception):
    """Base class for exceptions in this module."""
    pass

class OwnerAlreadyExistsError(VehicleError):
    """Exception raised when trying to set an owner that already exists."""
    def __init__(self, message="Owner already exists. Use change_owner method to change the owner."):
        self.message = message
        super().__init__(self.message)