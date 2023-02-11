import json
from aiohttp.web import HTTPClientError


class BaseHTTPException(HTTPClientError):
    status_code = -1

    def __init__(self, status_code: int, message: str, data=None):
        self._message = message
        self._data = data
        self.status_code = status_code
        self._response = self.generate_error_response()
        super().__init__(text=self._response, content_type="application/json")

    def generate_error_response(self):
        response = {
            "status_code": self.status_code,
            "message": self._message
        }

        if self._data:
            response['error'] = self._data

        return json.dumps(response)