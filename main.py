from http.client import HTTPException
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, User, Role, UserUpdateRequest

app = FastAPI()

db : List[User] = [
    User(
        id=UUID("f7948ddf-3dd5-4331-b403-7403a8af82ff"),
        first_name="Ugoo",
        middle_name= "Francis",
        last_name="Ezekoma",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("02b26778-021a-4f9c-9ce4-fad06acbfc59"),
        first_name="Oma",
        middle_name= "Mary",
        last_name="Orjiako",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    )
]

@app.get('/')
async def root():
    return {"Hello": "UgooKoma and Oma"}

@app.get('/maami')
async def fetch_users():
    return db

@app.post('/maami')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/maami/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/maami/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id:UUID):
    for user in db:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.first_name is not None:
            user.last_name = user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name = user_update.middle_name
        if user_update.roles is not None:
            user.roles = user_update.roles 
        return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
