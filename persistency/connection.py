from tortoise import Tortoise

class DBConnection:

    def __init__(self):
        self.db_url = "postgres://admin:admin@localhost:5432/backend"
        self.modules = {'models': ['persistency.models.member',
                                   'persistency.models.collection',
                                   'persistency.models.item',
                                   'persistency.models.credential']}

    async def __aenter__(self):
        await Tortoise.init(
            db_url=self.db_url,
            modules=self.modules
        )
        await Tortoise.generate_schemas()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await Tortoise.close_connections()
