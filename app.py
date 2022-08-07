from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user) #user tiene la funcion helloworld en la carpeta routes
