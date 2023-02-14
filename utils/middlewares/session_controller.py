from functools import wraps
from persistency.connection import DBConnection
from tortoise.transactions import in_transaction
from utils.exceptions.http_exceptions import InternalServerError
from tortoise.exceptions import OperationalError

class SessionDB:
    def __init__(self, function):
        self.function = function
        wraps(function)(self)

    async def __call__(self, *args, **kwargs):
        try:
            async with DBConnection():
                async with in_transaction() as conn:
                    result = await self.function(*args, **kwargs)
                return result
        except OperationalError as err:
            raise InternalServerError('Database operation error!')