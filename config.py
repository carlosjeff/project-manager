from os import getenv
from dotenv import load_dotenv

class Config:

    load_dotenv()

    APP_PORT = getenv('APP_PORT', default=8000)

    SECREY_KEY = getenv("SECREY_KEY", default="secret")

    DATABASE = getenv('DB', default="postgres")
    DATABASE_USER = getenv('DB_USER', default="admin")
    DATABASE_PASS = getenv('DB_PASS', default="admin")
    DATABASE_HOST = getenv('DB_HOST', default="localhost")
    DATABASE_PORT = getenv('DB_PORT', default=5432)
    DATABASE_NAME = getenv('DB_NAME', default="backend")
    DATABASE_URL = f"{DATABASE}://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    DATABASE_MODELS = {'models': ['persistency.models.member',
                                  'persistency.models.collection',
                                  'persistency.models.item',
                                  'persistency.models.credential']}

