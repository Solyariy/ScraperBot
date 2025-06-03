from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import certifi
from contextlib import contextmanager
load_dotenv()

uri = os.environ.get("MONGODB_URL")

@contextmanager
def get_client_manager():
    client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
    yield client
    client.close()

def get_client():
    client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
    yield client
    client.close()
