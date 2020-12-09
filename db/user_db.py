from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str

database_users = Dict[str, UserInDB]

database_users = {
    "raymansell": UserInDB(**{"username": "raymansell",
                              "password": "123456"}),
    "test": UserInDB(**{"username": "test",
                        "password": "root"})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
