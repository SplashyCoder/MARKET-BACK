

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Simulación de base de datos
fake_db = [
    {"id": 1, "name": "Item 1", "cuantity": 10, "price": 100, "ready": False},
    {"id": 2, "name": "Item 2", "cuantity": 5, "price": 200, "ready": True},
]

# Clase Item
class Item(BaseModel):
    id: int
    name: str
    cuantity: int
    price: int
    ready: bool

# Clase para actualizaciones parciales
class ItemUpdate(BaseModel):
    price: Optional[int] = None
    ready: Optional[bool] = None



mercado_db: List[Item] = [
    Item(id=1, name='Arroz',cuantity=1, price=0, ready=False),
    Item(id=2, name='Panela',cuantity=6, price=0, ready=False),
    Item(id=3, name='Cafe',cuantity=1, price=0, ready=False),
    Item(id=4, name='Galletas',cuantity=1, price=0, ready=False),
    Item(id=5, name='Mani',cuantity=4  , price=0, ready=False),
    Item(id=6, name='Sardinas',cuantity=3, price=0, ready=False),
    Item(id=7, name='Monchos(comida)',cuantity=4, price=0, ready=False),
    Item(id=8, name='Monchos',cuantity=2, price=0, ready=False),
    Item(id=9, name='Monchos(Arena)',cuantity=1, price=0, ready=False),
    Item(id=10, name='Pan',cuantity=2, price=0, ready=False),
    Item(id=11, name='Atun',cuantity=3, price=0, ready=False),
    Item(id=12, name='Aceite',cuantity=1, price=0, ready=False),
    Item(id=13, name='Leche',cuantity=4, price=0, ready=False),
    Item(id=14, name='Huevos',cuantity=4, price=0, ready=False),
    Item(id=15, name='Queso',cuantity=3, price=0, ready=False),
    Item(id=16, name='Jamon',cuantity=3, price=0, ready=False),
    Item(id=17, name='Yogurth',cuantity=2, price=0, ready=False),
    Item(id=18, name='Gelatina',cuantity=4, price=0, ready=False),
    Item(id=19, name='Lechera',cuantity=1, price=0, ready=False),
    Item(id=20, name='Salsa de tomate',cuantity=1, price=0, ready=False),
    Item(id=21, name='Mantequilla',cuantity=1, price=0, ready=False),
    Item(id=22, name='Deshodorante',cuantity=2, price=0, ready=False),
    Item(id=23, name='Cloro',cuantity=1, price=0, ready=False),
    Item(id=24, name='Limpia vidrios',cuantity=1, price=0, ready=False),
    Item(id=25, name='Shampoo',cuantity=2, price=0, ready=False),
    Item(id=26, name='Jabon(loza)',cuantity=3, price=0, ready=False),
    Item(id=27, name='Jabon(cuerpo)',cuantity=3, price=0, ready=False),
    Item(id=28, name='Guantes',cuantity=3, price=0, ready=False),
    Item(id=29, name='Cervilletas',cuantity=1, price=0, ready=False),
    Item(id=30, name='Crema dental',cuantity=2, price=0, ready=False),
    
    
    ]


# Función para buscar un ítem
def search_item(item_id: int) -> Optional[Item]:
    for item in mercado_db:
        if item.id == item_id:
            return item
    return None


@app.get('/')
async def root():
    return mercado_db

@app.get('/items/{item_id}')
async def search_item_by_id(item_id: int):
    return search_item(item_id)

# Endpoint PATCH para actualizar el ítem
@app.patch('/item/update/{item_id}')
async def update_item(item_id: int, updates: ItemUpdate):
    # Buscar el ítem
    item = search_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if updates.price is not None:
        item.price = updates.price
    if updates.ready is not None:
        item.ready = updates.ready

    return {"msg": "Item updated successfully", "item": item}
