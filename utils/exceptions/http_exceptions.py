from utils.exceptions.base_http_exceptions import BaseHTTPException


class BadRequest(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(400, message, date)


class NotFound(BaseHTTPException):
    def __init__(self, message: str, date=None):
        super().__init__(404, message, date)


