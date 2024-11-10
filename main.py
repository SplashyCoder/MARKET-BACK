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
    Item(id=1, name='arroz',cuantity=1, price=0, ready=False),
    Item(id=2, name='Huevos',cuantity=4, price=0, ready=False),
    Item(id=3, name='Salsa de tomate',cuantity=1, price=0, ready=True),
    Item(id=4, name='Aceite',cuantity=1, price=0, ready=False),
    Item(id=5, name='Atun',cuantity=3, price=0, ready=False),
    Item(id=6, name='Panela',cuantity=5, price=0, ready=True),
    Item(id=7, name='Monchos',cuantity=2, price=0, ready=False)
    
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