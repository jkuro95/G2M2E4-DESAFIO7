from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    usertype: str
    name: str
    lastname: str
    cedula: int

database_users = Dict[str, UserInDB]

database_users = {
    "raymansell": UserInDB(**{"username": "raymansell",
                              "password": "123456",
                              "usertype": "administrador",
                              "name": "Raymond",
                              "lastname": "Mansell",
                              "cedula": 13467890}),
    "nrueda": UserInDB(**{"username": "nrueda",
                          "password": "abcd",
                          "usertype": "empleado",
                          "name": "Néstor",
                          "lastname": "Rueda",
                          "cedula": 91234765})
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None


def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db


def get_all_users():
    return database_users.values()

