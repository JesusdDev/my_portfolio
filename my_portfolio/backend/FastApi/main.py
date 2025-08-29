from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from my_portfolio.routes import Route


app = FastAPI()

#Para iniciar el servicio: uvicorn main:app --reload+


