from db.user_db import UserInDB
from db.user_db import get_user

from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

# User Auth route
@api.post("/user/auth")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return { "Autenticado": False }
    
    return { "Autenticado": True }
