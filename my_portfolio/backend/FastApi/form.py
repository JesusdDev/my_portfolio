from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from my_portfolio.routes import Route


app = FastAPI()

#Para iniciar el servicio: uvicorn main:app --reload+

class Form(BaseModel):
    name: str
    email: EmailStr
    subject: list [str]
    message: str

form_list = []

@app.post("/")
async def get_message(form: Form):
    print(f"Mensje recibido de: {Form.name}")
    print(f"Asunto: {Form.subject}")
    print(f"Correo: {Form.email}")
    print(f"Mensaje: {Form.message}")
    form_list.append(form)
    return form_list

