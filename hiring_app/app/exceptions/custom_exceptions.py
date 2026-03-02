class HiringAppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class UserNotFoundException(HiringAppException):
    def __init__(self, message: str = "User not found"):
        super().__init__(message, status_code=404)

class JobNotFoundException(HiringAppException):
    def __init__(self, message: str = "Job not found"):
        super().__init__(message, status_code=404)

class ApplicationNotFoundException(HiringAppException):
    def __init__(self, message: str = "Application not found"):
        super().__init__(message, status_code=404)

class EmailAlreadyRegisteredException(HiringAppException):
    def __init__(self, message: str = "Email already registered"):
        super().__init__(message, status_code=400)
