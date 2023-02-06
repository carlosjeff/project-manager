from tortoise import Tortoise
from config import Config

class DBConnection:

    def __init__(self):
        self.db_url = Config.DATABASE_URL
        self.modules = Config.DATABASE_MODELS

    async def __aenter__(self):
        await Tortoise.init(
            db_url=self.db_url,
            modules=self.modules
        )
        await Tortoise.generate_schemas()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await Tortoise.close_connections()
