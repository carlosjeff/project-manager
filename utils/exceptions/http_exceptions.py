from utils.exceptions.base_http_exceptions import BaseHTTPException


class BadRequest(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(400, message, date)


class NotFound(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(404, message, date)


class Unauthorized(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(401, message, date)

class Forbidden(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(403, message, date)

class InternalServerError(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(500, message, date)



