from fastapi import APIRouter #permite definir las rutas por separado
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet #permite genrar una func que permite cifrar

key=Fernet.generate_key()
f=Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()#consulta a la db
                                                                                  #el id del usuario guardado
                                                                                  #y devuelve el objeto del
                                                                                  # objeto q ha guardado      
@user.get("/users/{id}")
def helloworld(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.get("/users")
def helloworld():
    return "Hola Mundo!!!"

@user.get("/users")
def helloworld():
    return "Hola Mundo!!!"