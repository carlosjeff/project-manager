from functools import wraps
from persistency.connection import DBConnection

class SessionDB:
    def __init__(self, function):
        self.function = function
        wraps(function)(self)

    async def __call__(self, *args, **kwargs):
        async with DBConnection() as _:
            result = await self.function(*args, **kwargs)

            return result