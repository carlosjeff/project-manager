from aiohttp.web import RouteTableDef
from typing import Any

class RouteTableCustom(RouteTableDef):

    def __init__(self, prefix):
        super().__init__()
        self.prefix = prefix

    def get(self, path: str, **kwargs: Any):
        return super().get(self.prefix + path, **kwargs)

    def post(self, path: str, **kwargs: Any):
        return super().post(self.prefix + path, **kwargs)

    def patch(self, path: str, **kwargs: Any):
        return super().patch(self.prefix + path, **kwargs)

    def delete(self, path: str, **kwargs: Any):
        return super().delete(self.prefix + path, **kwargs)
