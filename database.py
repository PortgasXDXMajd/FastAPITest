import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_CONNECTION = os.getenv("MONGO_CONNECTION")

client: AsyncIOMotorClient = None

def get_database():
    global client
    if client is None:
        client = AsyncIOMotorClient(MONGO_CONNECTION)
    return client['my-test-db']
