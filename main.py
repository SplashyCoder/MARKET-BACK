from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel
from config import add_cors

app = FastAPI()
add_cors(app)

#cambio

class Item(BaseModel):
    id: int
    name: str
    cuantity: int
    price : int
    ready: bool
    

mercado = [
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
@app.get('/')
async def root():
    return mercado

@app.get("/update/{item_id}")
def update_user(item_id: int, item: Item):
    # Busca el usuario en la base de datos
    user = next((u for u in mercado if u["id"] == item_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

    # Actualiza los datos del usuario
    # if item.name is not None:
    #     user["name"] = item.name
    # if item.ready is not None:
    #     user["ready"] = item.ready

    # return {"message": "User updated successfully", "user": user}