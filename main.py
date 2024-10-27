from fastapi import FastAPI
from pydantic import BaseModel
from config import add_cors

app = FastAPI()
add_cors(app)

class Item(BaseModel):
    id: int
    name: str
    cuantity: int
    

mercado = [
    Item(id=1, name='arroz',cuantity=1),
    Item(id=2, name='Huevos',cuantity=4),
    Item(id=3, name='Salsa de tomate',cuantity=1),
    Item(id=4, name='Aceite',cuantity=1),
    Item(id=5, name='Atun',cuantity=3),
    Item(id=6, name='Panela',cuantity=5),
    Item(id=7, name='Monchos',cuantity=2)
    
    ]
@app.get('/')
async def root():
    return mercado