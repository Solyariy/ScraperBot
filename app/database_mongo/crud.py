from typing import Any
from pymongo.database import Collection
from .client_starter import get_client_manager

def create(collection: Collection, movie: dict[str, Any]):
    return collection.insert_one(movie)

def read(collection: Collection, movie: dict[str, Any]):
    return collection.find_one(movie)

def update(collection: Collection, to_find: dict[str, Any], to_set):
    return collection.update_one(to_find, to_set)

def delete(collection: Collection, movie: dict[str, Any]):
    return collection.delete_one(movie)
