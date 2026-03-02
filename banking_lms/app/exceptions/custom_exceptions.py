class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ResourceNotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)

class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized access"):
        super().__init__(message, 401)
